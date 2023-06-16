from django.shortcuts import render, redirect
from .models import Hotel, Habitacion, ServicioHoteleria

def buscar_habitaciones(request):
    hoteles = Hotel.objects.all()
    return render(request, 'buscar_habitaciones.html', {'hoteles': hoteles})

def resultados_habitaciones(request):
    if request.method == 'POST':
        sucursal_id = request.POST.get('sucursal')
        personas = int(request.POST.get('personas'))
        
        habitaciones = Habitacion.objects.filter(
            idHotel=sucursal_id,
            capacidad__gte=personas
        )

        return render(request, 'resultados_habitaciones.html', {'habitaciones': habitaciones})

    # Redireccionar a la página de búsqueda de habitaciones si se accede directamente a la vista de resultados
    return redirect('buscar_habitaciones')


def servicios_subservicios(request):
    servicios = ServicioHoteleria.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})


def acerca_de(request):
    return render(request,'acerca_de.html',{})

def cuenta(request):
    return render(request,'cuenta.html',{})
