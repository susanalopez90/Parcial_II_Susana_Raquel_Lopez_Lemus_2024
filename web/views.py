from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Renderiza el archivo index.html en la carpeta templates
