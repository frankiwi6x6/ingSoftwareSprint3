from django.shortcuts import render, redirect
from .models import Hotel, Habitacion, ServicioHoteleria, Reserva
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from decimal import Decimal
from datetime import date
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
def buscar_habitaciones(request):
    hoteles = Hotel.objects.all()
    return render(request, "buscar_habitaciones.html", {"hoteles": hoteles})

def resultados_habitaciones(request):
    if request.method == "POST":
        sucursal_id = request.POST.get("sucursal")
        personas = request.POST.get("personas")

        fecha_entrada = request.POST.get("fecha-entrada")
        fecha_salida = request.POST.get("fecha-salida")

        errors = []

        if not fecha_entrada or not fecha_salida:
            errors.append("Debes ingresar ambas fechas.")

        if not personas or not personas.isdigit():
            errors.append("Debes ingresar un número válido en el campo de personas.")

        if fecha_entrada and fecha_salida:
            fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d")
            fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d")

            if fecha_entrada >= fecha_salida:
                errors.append(
                    "La fecha de entrada debe ser anterior a la fecha de salida."
                )

        if errors:
            hoteles = Hotel.objects.all()  # Obtener todos los hoteles
            return render(
                request,
                "buscar_habitaciones.html",
                {"errors": errors, "hoteles": hoteles},
            )

        habitaciones = Habitacion.objects.filter(
            idHotel=sucursal_id, capacidad__gte=int(personas)
        )

        hotel_slug = sucursal_id  # Asignar el valor de sucursal_id a hotel_slug

        fecha_entrada = request.POST.get("fecha-entrada")
        fecha_salida = request.POST.get("fecha-salida")
        personas = request.POST.get("personas")

        # Agregar los valores al contexto
        context = {
            "habitaciones": habitaciones,
            "hotel_slug": hotel_slug,
            "fecha_entrada": fecha_entrada,
            "fecha_salida": fecha_salida,
            "personas": personas,
        }
        print("Contexto:", context)

        return render(request, "resultados_habitaciones.html", context)

    hoteles = Hotel.objects.all()  # Obtener todos los hoteles
    return render(request, "buscar_habitaciones.html", {"hoteles": hoteles})

def reservar_habitacion(request):
    if request.method == "POST":
        entrada = request.POST.get("entrada")
        salida = request.POST.get("salida")

        # Convertir las fechas de entrada y salida a objetos de fecha
        entrada = datetime.strptime(entrada, "%Y-%m-%d").date()
        salida = datetime.strptime(salida, "%Y-%m-%d").date()

        # Aquí puedes realizar cualquier otra acción que necesites con la duración de la estancia y el costo total

        return redirect(
            "pagina_reserva"
        )  # Redireccionar a la página de reserva exitosa

    return render(request, "reservar_habitacion.html")

def realizar_reserva(request, hotel_slug, habitacion_slug):
    hotel_id = hotel_slug
    nHabitacion = int(habitacion_slug)

    hotel = Hotel.objects.get(idHotel=hotel_id)
    habitacion = Habitacion.objects.get(idHotel=hotel_id, numeroHabitacion=nHabitacion)

    context = {}

    if request.method == "POST":
        confirmado = False
        checkin = request.POST.get("fecha_entrada")
        checkout = request.POST.get("fecha_salida")

        if checkin is not None and checkout is not None:
            fecha_entrada = datetime.strptime(checkin, "%Y-%m-%d")
            fecha_salida = datetime.strptime(checkout, "%Y-%m-%d")
        personas = int(request.POST.get("personas"))
        if personas is not None:
                    personas = int(personas)

        dias_estancia = (fecha_salida - fecha_entrada).days

        total = (
            Decimal(habitacion.precioPorNoche)
            * Decimal(personas)
            * Decimal(dias_estancia)
        )
        
        context = {
            "fecha_entrada": checkin,
            "fecha_salida": checkout,
            "hotel": hotel,
            "habitacion": habitacion,
            "personas": personas,
            "dias_estancia": dias_estancia,
            "total": total,
        }

        # Guardar la reserva en la base de datos
        # Verificar si se ha confirmado la reserva
        
    return render(request, "realizar_reserva.html",context)
          
def crear_reserva(request):
    if request.method == "POST":
        # Obtener los datos enviados por el formulario
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        hotel_id = request.POST.get("hotel_id")
        habitacion_id = request.POST.get("habitacion_id")
        checkin = request.POST.get("checkin")
        checkout = request.POST.get("checkout")
        estancia = request.POST.get("estancia")
        total = int(request.POST.get("total"))
        nombre_usuario = request.POST.get("usuario")

    
        hotel = Hotel.objects.get(idHotel=hotel_id)
        habitacion = Habitacion.objects.get(idHabitacion=habitacion_id)
        
        # Obtener la instancia de User correspondiente al nombre de usuario
        usuario = User.objects.get(username=nombre_usuario)

        reserva = Reserva(
            idHotel=hotel,
            habitacion=habitacion,
            fecha_entrada=checkin,
            fecha_salida=checkout,
            dias_estancia=estancia,
            total=total,
            usuario=usuario,  # Asignar la instancia de User en lugar del nombre de usuario
        )
        reserva.save()
        
        return redirect('/servicios/?notificacion=exitosa')

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


@login_required
def perfil(request):
    usuario = request.user  # Obtener el usuario autenticado
    
    # Filtrar todas las reservas del usuario por nombre de usuario
    reservas = Reserva.objects.filter(usuario__username=usuario.username)
    
    # Filtrar la reserva actual del usuario por fecha de reserva actual
    reserva_actual = Reserva.objects.filter(usuario__username=usuario.username, fecha_entrada__lte=timezone.now(), fecha_salida__gte=timezone.now()).first()
    
    # Obtener información adicional del usuario
    nombre = usuario.first_name
    apellido = usuario.last_name
    nombre_usuario = usuario.username
    email = usuario.email
    context = {
        'reservas': reservas,
        'reserva_actual': reserva_actual,
        'nombre': nombre,
        'apellido': apellido,
        'nombre_usuario': nombre_usuario,
        'email' : email,
        'errores': get_error_messages(request),  # Obtener solo los mensajes de error
        'exitos': get_success_messages(request),  # Obtener solo los mensajes de éxito
    }
    
    return render(request, 'perfil.html', context)
def get_success_messages(request):
    """
    Retorna una lista de mensajes de éxito del objeto messages.
    """
    success_messages = []
    for message in messages.get_messages(request):
        if message.level == messages.SUCCESS:
            success_messages.append(message)
    return success_messages

from django.contrib import messages

def get_error_messages(request):
    """
    Retorna una lista de mensajes de error del objeto messages.
    """
    error_messages = []
    for message in messages.get_messages(request):
        if message.level == messages.ERROR:
            error_messages.append(message)
    return error_messages


@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        contrasena_actual = request.POST.get('contrasena_actual')
        nueva_contrasena = request.POST.get('nueva_contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')

        # Validar las contraseñas y realizar el cambio si son válidas
        if request.user.check_password(contrasena_actual):
            if nueva_contrasena == confirmar_contrasena:
                request.user.set_password(nueva_contrasena)
                request.user.save()
                messages.success(request, 'Contraseña cambiada correctamente.')
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
        else:
            messages.error(request, 'Contraseña actual incorrecta.')

        return redirect('perfil')
    else:
        return redirect('perfil')

def detalle_reserva(request):
    

    return render(request, 'detalle_reserva.html')

def cerrar_sesion(request):
    logout(request)
    return redirect("buscar_habitaciones")