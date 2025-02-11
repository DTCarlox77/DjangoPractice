from django.shortcuts import render, HttpResponse

def main(request):
    
    nombre = 'Luisa'
    
    variable = ['Python', 'JavaScript', 'C++']
    objetos = ['Carro', 'Teléfono', 'Computadora', 'Lámpara']
    # Render recibe 3 parámetros:
    # 1. request
    # 2. nombre del HTML a renderizar
    # 3. JSON o un diccionario con información (Opcional)
    return render(request, 'pages/main.html', {
        'variable' : variable,
        'objetos' : objetos,
        'nombre' : nombre
    })
    
frutas = []

def frutas_view(request):
    mensaje = None
    
    # POST: Envío de datos
    if request.method == 'POST':
        fruta = request.POST.get('fruta')
        if len(fruta.strip()) == 0:
            mensaje = 'No se puede almacenar una fruta vacía'

        elif not fruta.isalpha():
            mensaje = 'No se pueden almacenar números'
            
        else:
            frutas.append(fruta)
    
    return render(request, 'pages/frutas.html', {
        'frutas' : frutas,
        'error' : mensaje
    })
    
def fruta_view(request, index):
    fruta = frutas[index]
    
    return render(request, 'pages/fruta.html', {
        'fruta' : fruta
    })
    
#Vista para la lista de usuarios

users = []

def user_view(request):
    mensaje = None
    if request.method == 'POST':
        user = request.POST.get('user')
        if user in users:
            mensaje = 'El usuario ya existe'
        else:
            users.append(user)
    
    return render(request, 'pages/users.html', {
        'users' : users,
        'error' : mensaje
    })