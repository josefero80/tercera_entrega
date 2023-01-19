from django.shortcuts import render
from app_entrega.models import Alimento, Accesorio, Juguete
# Create your views here.
def home(request):
    return render(request, 'app_entrega/index.html', )

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