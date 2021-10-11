from django.db import models
from usuarios.models import Usuario
from datetime import datetime


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    thumb = models.ImageField(upload_to="thumb_cursos")

    def __str__(self) -> str:
        return self.nome


class Aula(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    aula = models.FileField(upload_to="aulas")
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome


class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    comentario = models.TextField()
    data = models.DateTimeField(default=datetime.now)
    aula = models.ForeignKey(Aula, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.usuario.nome


class NotaAula(models.Model):
    choices = (
        ('p', 'Péssimo'),
        ('r', 'Ruim'),
        ('re', 'Regular'),
        ('b', 'bom'),
        ('o', 'Ótimo')
    )

    aula = models.ForeignKey(Aula, on_delete=models.DO_NOTHING)
    nota = models.CharField(max_length=50, choices=choices)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
