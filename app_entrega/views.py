from django.shortcuts import render, redirect
from app_entrega.models import Alimento, Accesorio, Juguete
from django.urls import reverse, reverse_lazy
# Create your views here.
def home(request):
    return render(request, 'app_entrega/index.html', )

#Funciones para seccion alimentos:

def alimentos(request):
    contexto = {'alimentos': Alimento.objects.all()}
    return render(request, 'app_entrega/alimento.html', contexto,)

def res_buscar_al(request):
    producto = request.GET.get('busqueda_al')
    if producto:

        articulo = Alimento.objects.filter(nombre_al__icontains = producto)
        contexto = {'query': producto, 'articulo': articulo}
        
        return render(request, 'app_entrega/buscar_alim.html', contexto, )

    
    else:
        contexto = {'articulo_buscado': 'No hay ningun producto requerido'}
        return render(request, 'app_entrega/buscar_alim.html', contexto, )

def insertar_alimento(request):
    if request.method == 'POST':
        data = request.POST
        nuevo_alimento = Alimento(nombre_al = data["nombreAl"], categoria_al = data["categoriaAl"], precio_al = data["precioAl"])
        nuevo_alimento.save()
        url_exitosa = reverse('alimento_mascotas')
        return redirect(url_exitosa)
    else:
        return render(request, 'app_entrega/ingresa-alm.html', )
    
#Funciones para seccion accesorios:

def accesorios(request):
    contexto = {'accesorios': Accesorio.objects.all()}
    return render(request, 'app_entrega/accesorios.html', contexto)

def res_buscar_acc(request):
    producto_query = request.GET["query_acc"]

    if producto_query:

        accesorio = Accesorio.objects.filter(nombre_ac__icontains=producto_query)
        contexto = {'query': producto_query, 'accesorios': accesorio}
        return render(request, 'app_entrega/buscar_acc.html', contexto,)
    
    else:
        contexto = {'mensaje': 'No ingresaste ninguna busqueda... '}
    
    return render(request, 'app_entrega/buscar_acc.html', {'mensaje': contexto},)

def insertar_accesorio(request):
    if request.method == 'POST':
        data = request.POST
        nuevo_accesorio = Accesorio(nombre_ac = data["nombreAc"], categoria_ac = data["categoriaAc"], precio_ac = data["precioAc"])
        nuevo_accesorio.save()
        url_exitosa = reverse('accesorios_mascotas')
        return redirect(url_exitosa)
    else:
        return render(request, 'app_entrega/ingresa-acc.html', )

#Funciones para seccion juguetes:

def juguetes(request):
    contexto = {'juguetes': Juguete.objects.all()}
    return render(request, 'app_entrega/juguetes.html', contexto,)

def res_buscar_ju(request):
    producto = request.GET.get('query_ju')
    if producto:

        articulo = Juguete.objects.filter(nombre_ju__icontains = producto)
        contexto = {'query': producto, 'articulo': articulo}
        
        return render(request, 'app_entrega/buscar_ju.html', contexto, )

    
    else:
        contexto = {'articulo_buscado': 'No hay ningun producto requerido'}
        return render(request, 'app_entrega/buscar_ju.html', contexto, )

def insertar_ju(request):
    if request.method == 'POST':
        data = request.POST
        nuevo_juguete = Juguete(nombre_ju = data["nombreJu"], categoria_ju = data["categoriaJu"], precio_ju = data["precioJu"])
        nuevo_juguete.save()
        url_exitosa = reverse('juguete_mascotas')
        return redirect(url_exitosa)
    else:
        return render(request, 'app_entrega/ingresa-ju.html', )