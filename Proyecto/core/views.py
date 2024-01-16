from django.shortcuts import redirect, render
from . import models
from . import forms 
from . models import Profesor, Estudiante


def index(request):
    return render(request, "core/index.html")

def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "core/profesor_list.html", contexto) 

def profesor_create(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesor_list")
    else:
        form = forms.ProfesorForm()
    return render(request, "core/profesor_create.html", {"form": form})

def estudiante_list(request):
    consulta = models.Estudiante.objects.all()
    contexto = {"estudiantes": consulta}
    return render(request, "core/estudiante_list.html", contexto) 

def estudiante_create(request):
    if request.method == "POST":
        form = forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_list")
    else:
        form = forms.EstudianteForm()
    return render(request, "core/estudiante_create.html", {"form": form})