new WOW().init();




$(window).scroll(function() {
    if ($("#menu ").offset().top > 10) {
        $("#menu ").addClass("activar ");
    } else {
        $("#menu ").removeClass("activar ");
    }
});

function numeros(e) {
    key = e.keyCode || e.which;
    teclado = String.fromCharCode(key);

    numero = "0123456789";
    especiales = "8-37-38-46";
    tecla_especial = false;
    for (var i in especiales) {
        if (key == especiales[i])
            tecla_especial = true;
    }
    if (numero.indexOf(teclado) == -1 && !tecla_especial) {
        return false;
    }


}

function letra(e) {

    var key = e.keyCode || e.which,
        tecla = String.fromCharCode(key).toLowerCase();

    letras = " áéíóúabcdefghijklmnñopqrstuvwxyz",

        especiales = [8, 37, 39, 46],
        tecla_especial = false;

    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;

        }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    }
}