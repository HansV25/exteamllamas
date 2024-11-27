from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.pedido_home, name='home'),

    path('seleccionarCrud/', views.seleccionar_crud_pedido, name='seleccionar_crud_pedido'),

    path('crear-pedido/', views.crear_pedido, name='crear_pedido'),
    path('lista-pedidos/', views.pedido_home, name='pedido_home'),
    path('editar-pedido/<int:pk>/', views.editar_pedido, name='editar_pedido'),
    path('detalle-pedido/<int:pk>/', views.detalle_pedido, name='detalle_pedido'),
    path('eliminar-pedido/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
]
