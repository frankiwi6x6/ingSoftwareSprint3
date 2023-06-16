from django.urls import path
from . import views

urlpatterns = [
    # ... otras URLs de tu aplicación ...

    path('', views.buscar_habitaciones, name='buscar_habitaciones'),
    path('resultados_habitaciones/', views.resultados_habitaciones, name='resultados_habitaciones'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('servicios/', views.servicios_subservicios, name='servicios'),
    path('cuenta/', views.cuenta, name='cuenta'),
]