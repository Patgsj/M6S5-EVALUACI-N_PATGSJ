from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros/', views.libros, name='libros'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('contacto/', views.contacto, name='contacto'),
]
