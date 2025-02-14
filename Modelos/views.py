from django.shortcuts import render, redirect, get_object_or_404
from .models import Fruta

# Create your views here.
def main(requets):
    frutas = Fruta.objects.all()
    
    return render(requets, 'pages/main.html', {
        'frutas' : frutas
    })
    
def visitar_fruta(request, id):
    
    fruta = get_object_or_404(Fruta, id=id)
    # HTTP RESPONSE: 200 -> Éxito, 300 -> Redirección, 400 -> Errores del cliente, 500 -> Errores del servidor
    return render(request, 'pages/fruta.html', {
        'fruta': fruta
    })
    
def buscar_frutas(request):
    frutas = None
    
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        
        try:
            # Similar al %ILIKE% en SQL
            frutas = Fruta.objects.filter(nombre__contains=nombre)
        
        except Exception as e:
            print(f'Error: {e}')
        
    return render(request, 'pages/main.html', {
        'frutas' : frutas,
        'busqueda': True
    })
    
def eliminar_fruta(request, id):
    
    fruta = get_object_or_404(Fruta, id=id)
    fruta.delete()
    
    return redirect('main')
    
def agregar_fruta(request):
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        
        try:
            fruta = Fruta.objects.create(nombre=nombre, precio=precio)
            fruta.save()
            
        except Exception as e:
            print(f'Ocurrió un error: {e}')
            
    return redirect('main')

def error(request):
    
    return render(request, 'errors/404.html')