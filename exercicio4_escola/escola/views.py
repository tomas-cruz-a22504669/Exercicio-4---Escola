from django.shortcuts import render

# Create your views here.
from .models import Curso, Estudante

def lista_cursos(request):
    cursos = Curso.objects.select_related('professor').prefetch_related('estudantes')
    return render(request, 'cursos.html', {'cursos': cursos})

def lista_estudantes(request):
    estudantes = Estudante.objects.prefetch_related('cursos')
    return render(request, 'estudantes.html', {'estudantes': estudantes})