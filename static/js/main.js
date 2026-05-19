

async function comprobarLogin() {

    const parametros = new URLSearchParams(window.location.search);

    const token = parametros.get("token");


    if (!token) {
        alert("Pagina sin token");
        document.getElementById("botonNuevo").style.display = "none";
        return;
    }

    const respuesta = await fetch("http://127.0.0.1:8000/comprobar/", {

        headers: {
            "Authorization": "Bearer " + token
        }
    });

    if (!respuesta.ok) {
        alert("No estas Logeado");

        document.getElementById("botonNuevo").style.display = "none";
    }
    else {
        alert("Estas Logeado");
    }
}
comprobarLogin();

const formulario = document.querySelector('form:not(.formbuscador)');

if (formulario) {
    formulario.onsubmit = function () {
        alert("Formulario enviado correctamente");
    };
}
