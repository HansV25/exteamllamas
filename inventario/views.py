from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Extintor
from .forms import ExtintorForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.

@login_required
def seleccionar_crud_inventario(request):
    if request.user.perfil.rol in ['tecnico', 'administrador']:
        extintores = Extintor.objects.all()  
        return render(request, 'inventario/seleccionar_crud_inventario.html', {'extintores': extintores})
    else:
        return redirect('inventario:lista_clientes')  

#.......LISTA de Items..........
@login_required
def inventario_home(request):
    q = request.GET.get('q', '')
    if q:
        extintores = Extintor.objects.filter(
            Q(nombre__icontains=q) | Q(tipo__icontains=q)
        )
    else:
        extintores = Extintor.objects.all()
    return render(request, 'inventario/inventario_home.html', {'extintores': extintores, 'q': q})

#................vista para crear inventario...................
@login_required
def crear_extintor(request):
    if request.user.perfil.rol in ['administrador', 'tecnico']:
        if request.method == 'POST':
            form = ExtintorForm(request.POST)
            if form.is_valid():
                Extintor = form.save(commit=False)
                Extintor.save() 
                return redirect('inventario:detalle_extintor', pk=Extintor.pk)
        else:
            form = ExtintorForm()
        return render(request, 'Inventario/crear_extintor.html', {'form': form})
    else:
        return redirect('inventario:inventario_home')


#........Ventana de detalles........
@login_required
def detalle_extintor(request, pk):
    if request.user.perfil.rol in ['tecnico', 'administrador']:
        extintor = get_object_or_404(Extintor, pk=pk)
        return render(request, 'inventario/detalle_extintor.html', {'extintor': extintor})

@login_required
def editar_extintor(request, pk):
    extintor = get_object_or_404(Extintor, pk=pk)
    if request.user.perfil.rol in ['administrador', 'tecnico']:
        if request.method == 'POST':
            form = ExtintorForm(request.POST, instance=extintor)
            if form.is_valid():
                form.save()
                messages.success(request, '¡Cambios guardados exitosamente!', extra_tags='cliente')
                return redirect('inventario:inventario_home')
        else:
            form = ExtintorForm(instance=extintor)
        return render(request, 'Inventario/editar_extintor.html', {'form': form})
    else:
        return redirect('inventario:inventario_home')



@login_required
def eliminar_extintor(request, extintor_id):
    extintor = Extintor.objects.get(id=extintor_id)
    extintor.delete()
    return redirect('inventario:inventario_home')