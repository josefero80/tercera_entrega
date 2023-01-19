from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('/alimento-mascotas/', views.alimentos, name='alimento_mascotas'),
    path('/resultado-busqueda-alimento/', views.res_buscar_al, name='buscar_al')
   
]