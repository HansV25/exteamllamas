from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('detalle/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),



    path('seleccionar/', views.seleccionar_crud_cliente, name='seleccionar_crud_cliente'),

    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('lista/', views.lista_clientes, name='lista_clientes'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),

]
