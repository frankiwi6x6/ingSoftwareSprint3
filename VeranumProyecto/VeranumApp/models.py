from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    idHotel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    num_habitaciones = models.IntegerField()

    def __str__(self):
        return self.nombre

class TipoHabitacion(models.Model):
    idTipoHabitacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400)

    def __str__(self):
        return self.nombre

class Habitacion(models.Model):
    idHotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    idHabitacion = models.AutoField(primary_key=True)
    numeroHabitacion = models.IntegerField(null=False)
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    capacidad = models.IntegerField(null=False)
    precioPorNoche = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=200)
    is_disponible = models.BooleanField(default=True)
    imagen = models.ImageField(default='static/img/habitacion-prueba.jpg', upload_to='static/img')

    class Meta:
        unique_together = ('idHotel', 'numeroHabitacion')

    def __str__(self):
        return f'{self.tipo.nombre} - {self.idHotel.nombre}'

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    idHotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.CharField(max_length=9)
    fecha_salida = models.CharField(max_length=9)
    dias_estancia = models.IntegerField()
    total = models.DecimalField(max_digits=15, decimal_places=0)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva ({self.idReserva}) de {self.usuario.username} " 
    


class ServicioHoteleria(models.Model):
    idServicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Subservicio(models.Model):
    idSubservicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400)
    horarioApertura = models.TimeField()
    horarioCierre = models.TimeField()
    servicio = models.ForeignKey(ServicioHoteleria, on_delete=models.CASCADE)
    imagen = models.ImageField(default='static/img/servicio_prueba.jpg', upload_to='static/img')

    def __str__(self):
        return self.nombre

