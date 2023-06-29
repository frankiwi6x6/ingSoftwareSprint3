from django.urls import path
from . import views

urlpatterns = [
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
    path('crear_reserva/', views.crear_reserva, name='crear_reserva'),
    path('perfil/',views.perfil, name='perfil'),
    path('cambiar_contrasena', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('accounts/login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('eliminar_reserva/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
    path('crear_subservicio/', views.crear_subservicio, name='crear_subservicio'),
    path('contacto/', views.contacto, name='contacto'),
    
]