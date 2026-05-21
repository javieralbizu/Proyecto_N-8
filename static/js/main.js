let tamano = 20;

async function comprobarLogin() {

    const parametros = new URLSearchParams(window.location.search);

    const token = parametros.get("token");


    if (!token) {
        alert("Pagina sin token");
        let privado = document.getElementsByClassName("privado")
        for (let i = 0; i < privado.length; i++) {
            privado[i].style.display = "none";
        }
        return;
    }

    const respuesta = await fetch("http://127.0.0.1:8000/comprobar/", {

        headers: {
            "Authorization": "Bearer " + token
        }
    });

    if (!respuesta.ok) {
        alert("No estas Logeado");

        let privado = document.getElementsByClassName("privado")
        for (let i = 0; i < privado.length; i++) {
            privado[i].style.display = "none";
        }
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

function aumento() {
    if (tamano < 30) {
        tamano += 1;
        aplicarTamano();
    }
}

function disminuir() {
    if (tamano > 8) {
        tamano -= 1;
        aplicarTamano();
    }
}

const elementos = document.querySelectorAll('p,h1,th,td,a,button');

function aplicarTamano() {

    elementos.forEach(elemento => {
        elemento.style.fontSize = tamano + "px";
    });
}