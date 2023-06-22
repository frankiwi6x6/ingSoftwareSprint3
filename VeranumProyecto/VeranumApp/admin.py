from django.contrib import admin
from .models import Hotel, Habitacion, TipoHabitacion
from .models import ServicioHoteleria,Subservicio, Reserva
# Register your models here.



admin.site.register(Hotel)
admin.site.register(Habitacion)
admin.site.register(TipoHabitacion)
admin.site.register(ServicioHoteleria)
admin.site.register(Subservicio)
admin.site.register(Reserva)