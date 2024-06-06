from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Instalacion
from .forms import ClienteForm, InstalacionForm

def home(request):
    return render(request, 'servicios/home.html')

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'servicios/registrar_cliente.html', {'form': form})

def registrar_instalacion(request):
    if request.method == 'POST':
        form = InstalacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InstalacionForm()
    return render(request, 'servicios/registrar_instalacion.html', {'form': form})

def lista_instalaciones(request):
    instalaciones = Instalacion.objects.all()
    return render(request, 'servicios/lista_instalaciones.html', {'instalaciones': instalaciones})

def detalle_instalacion(request, pk):
    instalacion = get_object_or_404(Instalacion, pk=pk)
    return render(request, 'servicios/detalle_instalacion.html', {'instalacion': instalacion})
