from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('seleccionar-aplicacion/', views.seleccionar_aplicacion, name='seleccionar_aplicacion'),
    path('perfil/', views.perfil, name='perfil'),



]