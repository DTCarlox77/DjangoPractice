from django.urls import path
from .views import main, agregar_fruta, visitar_fruta, eliminar_fruta, buscar_frutas, error

urlpatterns = [
    path('', main, name='main'),
    path('add/', agregar_fruta, name='agregar_fruta'),
    path('fruta/<int:id>/', visitar_fruta, name='visitar_fruta'),
    path('eliminar/<int:id>/', eliminar_fruta, name='eliminar'),
    path('buscar/', buscar_frutas, name='buscar'),
    path('error/', error)
]
