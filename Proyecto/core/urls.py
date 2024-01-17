from django.urls import path 

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("profesor/list/", views.profesor_list, name="profesor_list"),
    path("profesor/create/", views.profesor_create, name="profesor_create"),
    path("estudiantes/list/", views.estudiante_list, name="estudiante_list"),
    path("estudiantes/create/", views.estudiante_create, name="estudiante_create"),
]

