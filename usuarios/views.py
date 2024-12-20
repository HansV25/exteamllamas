from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from .models import Perfil
from django.contrib import messages
from inventario.models import Extintor

# Create your views here.

#Index que se muestra en la url ''
def index(request):
    return render(request, 'usuarios/index.html')



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])

            user.save()
            user.perfil.rol = form.cleaned_data['rol']
            user.perfil.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')

            return redirect('usuarios:login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('usuarios:seleccionar_aplicacion')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'usuarios/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('usuarios:login')


@login_required
def perfil(request):
    perfil = Perfil.objects.get(user=request.user)
    return render(request, 'usuarios/perfil.html', {'perfil': perfil})


def contacto(request):
    return render(request)

# Al iniciar sesión como administrador/tecnico renderiza al panel de gestion
@login_required
def seleccionar_aplicacion(request):
    if request.user.perfil.rol in ['administrador', 'tecnico']:
        extintores_bajos = Extintor.objects.filter(cantidad__lt=10)
        if extintores_bajos.exists():
            mensajes = ", ".join([extintor.nombre for extintor in extintores_bajos])
            messages.warning(request, f"Los siguientes productos en el Inventario tienen un stock bajo de 10 unidades: {mensajes}")
        return render(request, 'usuarios/seleccionar_aplicacion.html')
    else:
        return redirect('usuarios:index') 