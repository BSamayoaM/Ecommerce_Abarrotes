from django.shortcuts import render

def productos(request):
    return render(request,'productos/inicio.html')
def crear_productos(request):
    return render(request,'productos/crear.html')
def editar_producto(request):
    return render(request,'productos/editar.html')
def ver_producto(request):
    return render(request,'productos/ver.html')
