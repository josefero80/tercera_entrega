from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('/alimento-mascotas/', views.alimentos, name='alimento_mascotas'),
    path('/resultado-busqueda-alimento/', views.res_buscar_al, name='buscar_al'),
    path('/accesorios-mascotas/', views.accesorios, name='accesorios_mascotas'  ),
    path('/resultado-busqueda-accesorios/', views.res_buscar_acc, name='buscar_acc'),
    path('/insertar-alimento', views.insertar_alimento, name='insertar_alimento'),
    path('/insertar-accesorio', views.insertar_accesorio, name='insertar_accesorio'),
    path('/juguetes-mascotas/', views.juguetes, name='juguete_mascotas'),
    path('/resultado-busqueda-juguetes/', views.res_buscar_ju, name='buscar_ju'),
    path('/insertar-juguete', views.insertar_ju, name='insertar_juguete'),
   
]