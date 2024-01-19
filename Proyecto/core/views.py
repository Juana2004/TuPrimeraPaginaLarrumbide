
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Profesor, Estudiante, Curso
from .forms import ProfesorForm, EstudianteForm

def index(request):
    return render(request, "core/index.html")

def profesor_list(request):
    consulta = Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "core/profesor_list.html", contexto) 

def profesor_create(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesor_list")
    else:
        form = ProfesorForm()
    return render(request, "core/profesor_create.html", {"form": form})

def estudiante_list(request):
    consulta = Estudiante.objects.all()
    contexto = {"estudiantes": consulta}
    return render(request, "core/estudiante_list.html", contexto) 

def estudiante_create(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_list")
    else:
        form = EstudianteForm()
    return render(request, "core/estudiante_create.html", {"form": form})

class CursoListView(ListView):
    model = Curso
    template_name = 'core/curso_list.html'  # Ajusta el nombre del template según tu estructura
    context_object_name = 'cursos'
