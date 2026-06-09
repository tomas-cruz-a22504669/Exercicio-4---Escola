from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Estudante(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    idioma = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='cursos')
    estudantes = models.ManyToManyField(Estudante, related_name='cursos')

    def __str__(self):
        return self.idioma