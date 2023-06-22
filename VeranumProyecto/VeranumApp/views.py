from django.shortcuts import render, redirect
from .models import Hotel, Habitacion, ServicioHoteleria, Reserva
from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def buscar_habitaciones(request):
    hoteles = Hotel.objects.all()
    return render(request, "buscar_habitaciones.html", {"hoteles": hoteles})


def resultados_habitaciones(request):
    if request.method == "POST":
        sucursal_id = request.POST.get("sucursal")
        personas = int(request.POST.get("personas"))

        habitaciones = Habitacion.objects.filter(
            idHotel=sucursal_id, capacidad__gte=personas
        )

        hotel_slug = sucursal_id  # Asignar el valor de sucursal_id a hotel_slug

        return render(
            request,
            "resultados_habitaciones.html",
            {"habitaciones": habitaciones, "hotel_slug": hotel_slug},
        )

    # Redireccionar a la página de búsqueda de habitaciones si se accede directamente a la vista de resultados
    return redirect("buscar_habitaciones")


from django.shortcuts import get_object_or_404


def realizar_reserva(request, hotel_slug, habitacion_slug):
    # Obtener el ID del hotel y el número de habitación del slug
    hotel_id = hotel_slug
    nHabitacion = int(habitacion_slug)

    # Obtener el objeto hotel y habitacion
    hotel = Hotel.objects.get(idHotel=hotel_id)
    habitacion = Habitacion.objects.get(idHotel=hotel_id, numeroHabitacion=nHabitacion)

    if request.method == "POST":
        # Obtener los datos del formulario de reserva
        fecha_entrada = request.POST.get("fecha-entrada")
        fecha_salida = request.POST.get("fecha-salida")

        # Resto del código para validar fechas, etc.

        if fecha_entrada and fecha_salida:
            # Realizar la reserva
            realizar_reserva_db(
                hotel, habitacion, fecha_entrada, fecha_salida, request.user
            )

            # Redirigir a una página de éxito de reserva o a otra vista
            return redirect("reserva_exitosa")

    # Si se accede a la vista por GET o si hay errores en los datos del formulario, renderizar el formulario de reserva
    return render(
        request,
        "realizar_reserva.html",
        {
            "hotel_slug": hotel_slug,
            "habitacion_slug": habitacion_slug,
            "hotel": hotel,
            "habitacion": habitacion,
        },
    )

def realizar_reserva_db(hotel, habitacion, fecha_entrada, fecha_salida, usuario):
    # Resto del código para calcular los días de estancia, realizar la reserva, etc.

    # Obtener el ID del hotel y el número de habitación
    hotel_id = hotel.idHotel
    nHabitacion = habitacion.numeroHabitacion

    # Calcular los días de estancia
    dias_estancia = (fecha_salida - fecha_entrada).days

    # Realizar la reserva
    reserva = Reserva.objects.create(
        idHotel=hotel_id,
        habitacion=habitacion,
        fecha_entrada=fecha_entrada,
        fecha_salida=fecha_salida,
        dias_estancia=dias_estancia,
        total=habitacion.precioPorNoche * dias_estancia,
        usuario=usuario,
    )

def servicios_subservicios(request):
    servicios = ServicioHoteleria.objects.all()
    return render(request, "servicios.html", {"servicios": servicios})


def acerca_de(request):
    return render(request, "acerca_de.html", {})


def registrarse(request):
    return render(request, "register.html", {})


def registro(request):
    if request.method == "POST":
        # Obtener los datos enviados por el formulario
        nombreDeUsuario = request.POST["nombre_usuario"]
        correo = request.POST["correo"]
        contraseña = request.POST.get("contraseña")
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]

        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=correo).exists():
            return HttpResponse(
                "El nombre de usuario ya existe. Por favor, elige otro nombre de usuario."
            )

        # Crear el nuevo usuario
        usuario = User.objects.create_user(
            username=nombreDeUsuario,
            email=correo,
            password=contraseña,
            first_name=nombre,
            last_name=apellido,
        )
        usuario.is_staff = False
        usuario.is_active = (
            True  # La cuenta se activará mediante el enlace de activación
        )

        usuario.save()

        return redirect(
            "buscar_habitaciones"
        )  # Redireccionar a una página de éxito de registro

    return render(request, "register.html")


def iniciar_sesion(request):
    if request.method == "POST":
        identificador = request.POST.get(
            "identificador"
        )  # Puede ser el nombre de usuario o el correo electrónico
        contraseña = request.POST["contraseña"]

        # Verificar si el identificador es un correo electrónico
        if "@" in identificador:
            # Intentar autenticar utilizando el correo electrónico
            try:
                usuario = User.objects.get(email=identificador)
                usuario = authenticate(
                    request, username=usuario.username, password=contraseña
                )
            except User.DoesNotExist:
                usuario = None
        else:
            # Intentar autenticar utilizando el nombre de usuario
            usuario = authenticate(request, username=identificador, password=contraseña)

        if usuario is not None:
            # El usuario existe y las credenciales son válidas
            login(request, usuario)
            return redirect("acerca_de")  # Redirigir a la página de inicio del usuario
        else:
            # El usuario no existe o las credenciales son inválidas
            error_message = (
                "Identificador o contraseña incorrectos. Por favor, inténtalo de nuevo."
            )
            return render(
                request, "iniciar_sesion.html", {"error_message": error_message}
            )
    else:
        return render(request, "iniciar_sesion.html")


def cerrar_sesion(request):
    logout(request)
    return redirect("buscar_habitaciones")


def reservar_habitacion(request):
    if request.method == "POST":
        entrada = request.POST.get("entrada")
        salida = request.POST.get("salida")
        precio_noche = request.POST.get("precio_noche")

        # Convertir las fechas de entrada y salida a objetos de fecha
        entrada = datetime.strptime(entrada, "%Y-%m-%d").date()
        salida = datetime.strptime(salida, "%Y-%m-%d").date()

        # Calcular la duración de la estancia en días
        duracion_estancia = (salida - entrada).days

        # Calcular el costo total de la estancia
        costo_total = duracion_estancia * float(precio_noche)

        # Aquí puedes realizar cualquier otra acción que necesites con la duración de la estancia y el costo total

        return redirect(
            "pagina_reserva"
        )  # Redireccionar a la página de reserva exitosa

    return render(request, "reservar_habitacion.html")
