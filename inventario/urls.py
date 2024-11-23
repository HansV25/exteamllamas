from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.inventario_home, name='home'),

    path('seleccionarCrud/', views.seleccionar_crud_inventario, name='seleccionar_crud_inventario'),

    path('crear-item/', views.crear_extintor, name='crear_extintor'),
    path('lista-inventario/', views.inventario_home, name='inventario_home'),
    path('editar-item/<int:pk>/', views.editar_extintor, name='editar_extintor'),
    path('detalle-item/<int:pk>/', views.detalle_extintor, name='detalle_extintor'),
    path('eliminar-extintor/<int:extintor_id>/', views.eliminar_extintor, name='eliminar_extintor'),

]
