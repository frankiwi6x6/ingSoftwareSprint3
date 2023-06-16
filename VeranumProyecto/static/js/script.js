document.addEventListener("DOMContentLoaded", function() {
    // Ocultar todos los formularios excepto el de registro al cargar la página
    $(".form-container").not("#registro").hide();

    // Agregar eventos de clic a los enlaces de cambio de formulario
    $("#enlace-registro").click(function(e) {
        e.preventDefault();
        mostrarFormulario("registro");
    });

    $("#enlace-login-registro").click(function(e) {
        e.preventDefault();
        mostrarFormulario("login");
    });

    $("#enlace-recuperar-registro").click(function(e) {
        e.preventDefault();
        mostrarFormulario("recuperar");
    });

    $("#enlace-login-login").click(function(e) {
        e.preventDefault();
        mostrarFormulario("login");
    });

    $("#enlace-registro-login").click(function(e) {
        e.preventDefault();
        mostrarFormulario("registro");
    });

    $("#enlace-recuperar-login").click(function(e) {
        e.preventDefault();
        mostrarFormulario("recuperar");
    });

    $("#enlace-registro-recuperar").click(function(e) {
        e.preventDefault();
        mostrarFormulario("registro");
    });

    $("#enlace-login-recuperar").click(function(e) {
        e.preventDefault();
        mostrarFormulario("login");
    });

    $("#enlace-recuperar").click(function(e) {
        e.preventDefault();
        mostrarFormulario("recuperar");
    });

    // Función para mostrar el formulario seleccionado
    function mostrarFormulario(formulario) {
        // Ocultar todos los formularios
        $(".form-container").hide();
        // Mostrar el formulario seleccionado
        $("#" + formulario).show();
    }
});
