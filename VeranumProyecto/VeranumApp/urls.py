from django.urls import path
from . import views

urlpatterns = [
    # ... otras URLs de tu aplicación ...

    path('', views.buscar_habitaciones, name='buscar_habitaciones'),
    path('resultados_habitaciones/', views.resultados_habitaciones, name='resultados_habitaciones'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('servicios/', views.servicios_subservicios, name='servicios'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('registro/', views.registro, name='registro'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('reservar_habitacion/', views.reservar_habitacion, name='reservar_habitacion'),
    path('realizar_reserva/<str:hotel_slug>-<str:habitacion_slug>/', views.realizar_reserva, name='realizar_reserva'),
]