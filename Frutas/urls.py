from django.urls import path
from .views import main, frutas_view, fruta_view

urlpatterns = [
    path('', main, name='main'),
    path('frutas/', frutas_view, name='frutas'),
    path('frutas/<int:index>/', fruta_view, name='fruta')
]
