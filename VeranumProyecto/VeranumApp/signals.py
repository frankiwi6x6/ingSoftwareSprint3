from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

@receiver(post_save, sender=Reserva)
def actualizar_disponibilidad_habitacion(sender, instance, created, **kwargs):
    if created:
        # Obtener la habitación asociada a la reserva
        habitacion = instance.habitacion
        # Obtener la fecha de salida de la reserva
        fecha_salida = instance.fecha_salida
        # Desactivar la disponibilidad de la habitación hasta la fecha de salida
        habitacion.is_disponible = False
        habitacion.save()