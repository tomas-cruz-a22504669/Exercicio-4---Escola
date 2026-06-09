from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.lista_cursos, name='cursos'),
    path('estudantes/', views.lista_estudantes, name='estudantes'),
]