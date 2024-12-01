from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
# Create your views here.

@login_required
def seleccionar_crud_cliente(request):
    if request.user.perfil.rol in ['tecnico', 'administrador']:
        clientes = Cliente.objects.all()  
        return render(request, 'Clientes/seleccionar_crud_cliente.html', {'clientes': clientes})
    else:
        return redirect('Clientes:lista_clientes')  

@login_required
def lista_clientes(request):
    q = request.GET.get('q', '')
    if q:
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=q) | Q(direccion__icontains=q) | Q(email__icontains=q) | Q(telefono__icontains=q)
        )
    else:
        clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes, 'q': q})

@login_required
def crear_cliente(request):
    if request.user.perfil.rol in ['administrador']:
        if request.method == 'POST':
            form = ClienteForm(request.POST)
            if form.is_valid():
                cliente = form.save(commit=False)
                cliente.save() 
                return redirect('clientes:detalle_cliente', pk=cliente.pk)
        else:
            form = ClienteForm()
        return render(request, 'Clientes/crear_cliente.html', {'form': form})
    else:
        return redirect('clientes:lista_clientes')

@login_required
def detalle_cliente(request, pk):
    if request.user.perfil.rol in ['tecnico', 'administrador']:
        cliente = get_object_or_404(Cliente, pk=pk)
        return render(request, 'Clientes/detalle_cliente.html', {'cliente': cliente})


@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.user.perfil.rol in ['administrador']:
        if request.method == 'POST':
            form = ClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                messages.success(request, '¡Cambios guardados exitosamente!', extra_tags='cliente')
                return redirect('clientes:lista_clientes')
        else:
            form = ClienteForm(instance=cliente)
        return render(request, 'Clientes/editar_cliente.html', {'form': form})
    else:
        return redirect('clientes:lista_clientes')

@login_required
def eliminar_cliente(request, pk):
    if request.user.perfil.rol in ['administrador']:
        cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes:lista_clientes')
    return render(request, 'Clientes/eliminar_cliente.html', {'cliente': cliente})

