from django.contrib import admin
from . import models

admin.site.register(models.Curso)
admin.site.register(models.CursoEstudiantes)
admin.site.register(models.Estudiante)
admin.site.register(models.Profesor)