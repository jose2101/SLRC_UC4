from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,"index.html",{}) 


def Integrantes(request):

    integrantes=['Piero Sayas','Leandro Luigui','Oscar Reyes','Jose Chavez']
    return render(request,"integrantes.html",{"integrantes":integrantes})

def Saludo(request):
    mensaje="Buen dia, le saluda los integrantes del grupo"
    return render(request,"saludo.html",{"mensaje":mensaje})