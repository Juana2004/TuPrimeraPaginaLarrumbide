from django.shortcuts import redirect, render
from . import models
from . import forms 
from . models import Profesor

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