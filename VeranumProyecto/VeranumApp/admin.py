from django.contrib import admin
from .models import Hotel, Habitacion, TipoHabitacion,ServicioHoteleria,Subservicio
# Register your models here.


admin.site.register(Hotel)
admin.site.register(Habitacion)
admin.site.register(TipoHabitacion)
admin.site.register(ServicioHoteleria)
admin.site.register(Subservicio)