from django.contrib import admin
from .models import Curso, Aula, Comentario, NotaAula

admin.site.register(Curso)
admin.site.register(Aula)
admin.site.register(Comentario)
admin.site.register(NotaAula)
