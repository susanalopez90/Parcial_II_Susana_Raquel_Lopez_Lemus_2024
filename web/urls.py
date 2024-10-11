from django.urls import path
from . import views  # Importa las vistas desde views.py

urlpatterns = [
    path('', views.home, name='home'),  # La ruta raíz (/) llama a la vista home
]