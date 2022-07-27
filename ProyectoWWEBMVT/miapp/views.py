from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Estudiante

# Create your views here.
def Index(request):
    return render(request,"index.html",{}) 


def Integrantes(request):

    integrantes=['Piero Sayas','Leandro Luigui','Oscar Reyes','Jose Chavez']
    return render(request,"integrantes.html",{"integrantes":integrantes})

def Saludo(request):
    mensaje="Buen dia, le saluda los integrantes del grupo"
    return render(request,"saludo.html",{"mensaje":mensaje})

def crear_estudiante(request):
    estudiante = Estudiante(
    codigo = "0123",
    dni = "2345",
    nombre = "Jose",
    apepat = "Martinez",
    apemat = "Lopez",
    direccion = "Av.128 Lima",
    telefono = "2870933",
    estado = "soltero",
    )
    estudiante.save()
    return HttpResponse(f"Estudiante Creado: {estudiante.codigo} - {estudiante.dni} - {estudiante.nombre} - {estudiante.apepat} - {estudiante.apemat} - {estudiante.direccion} - {estudiante.telefono} - {estudiante.estado} ")

   