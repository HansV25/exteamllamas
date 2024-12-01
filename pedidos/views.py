from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido
from .forms import PedidoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.

@login_required
def seleccionar_crud_pedido(request):
    if request.user.perfil.rol in ['tecnico', 'administrador']:
        pedidos = Pedido.objects.all()  
        return render(request, 'pedidos/seleccionar_crud_pedido.html', {'pedidos': pedidos})
    else:
        return redirect('pedidos:pedido_home') 

@login_required
def pedido_home(request):
    query = request.GET.get('q')
    if query:
        pedidos = Pedido.objects.filter(
            Q(cliente__nombre__icontains=query) |
            Q(item_inventario__nombre__icontains=query)
        )
    else:
        pedidos = Pedido.objects.all()
    return render(request, 'pedidos/pedido_home.html', {'pedidos': pedidos})

# crear el pedido
@login_required
def crear_pedido(request):
    if request.user.perfil.rol in ['administrador', 'tecnico']:
        if request.method == 'POST':
            form = PedidoForm(request.POST)
            if form.is_valid():
                pedido = form.save(commit=False)
                pedido.save()
                messages.success(request, 'Pedido creado exitosamente')
                return redirect('pedidos:pedido_home')
        else:
            form = PedidoForm()
        return render(request, 'pedidos/crear_pedido.html', {'form': form})
    else:
        return redirect('pedidos:pedido_home')


@login_required
def detalle_pedido(request, pk):
    if request.user.perfil.rol in ['tecnico', 'administrador']:
        pedido = get_object_or_404(Pedido, pk=pk)
        return render(request, 'pedidos/detalle_pedido.html', {'pedido': pedido})
    else:
        return redirect('pedidos:pedido_home')


@login_required
def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.user.perfil.rol in ['administrador', 'tecnico']:
        if request.method == 'POST':
            form = PedidoForm(request.POST, instance=pedido)
            if form.is_valid():
                form.save()
                messages.success(request, 'Pedido actualizado exitosamente')
                return redirect('pedidos:pedido_home')
        else:
            form = PedidoForm(instance=pedido)
        return render(request, 'pedidos/editar_pedido.html', {'form': form})
    else:
        return redirect('pedidos:pedido_home')


@login_required
def eliminar_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    pedido.delete();
    return redirect('pedidos:pedido_home')
