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

document.addEventListener("DOMContentLoaded", function () {

    const formulario = document.querySelector("form");
    const boton = formulario.querySelector("button");

    const campos = formulario.querySelectorAll("input");

    boton.disabled = true;

    campos.forEach(campo => {

        // Crear mensaje de error
        const error = document.createElement("small");
        error.style.color = "red";
        error.style.display = "block";

        campo.parentNode.appendChild(error);

        campo.addEventListener("input", function () {

            validarCampo(campo, error);
            validarFormulario();
        });
    });

    function validarCampo(campo, error) {

        let valido = false;

        // DNI
        if (campo.name === "DNI") {

            valido = /^[0-9]{8}[A-Za-z]$/.test(campo.value);

            error.textContent = valido ? "" : "DNI incorrecto";
        }

        // Nombre
        else if (campo.name === "Nombre") {

            valido = campo.value.length >= 2;

            error.textContent = valido ? "" : "Nombre demasiado corto";
        }

        // Apellido
        else if (campo.name === "Apellido") {

            valido = campo.value.length >= 2;

            error.textContent = valido ? "" : "Apellido demasiado corto";
        }

        // Email
        else if (campo.name === "Email") {

            valido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(campo.value);

            error.textContent = valido ? "" : "Email incorrecto";
        }

        // Telefono
        else if (campo.name === "Telefono") {

            valido = /^[0-9]{9}$/.test(campo.value);

            error.textContent = valido ? "" : "Telefono incorrecto";
        }

        campo.style.border = valido
            ? "2px solid green"
            : "2px solid red";

        return valido;
    }

    function validarFormulario() {

        let formularioValido = true;

        campos.forEach(campo => {

            const error = campo.parentNode.querySelector("small");

            if (!validarCampo(campo, error)) {
                formularioValido = false;
            }
        });

        boton.disabled = !formularioValido;
    }

});

document.addEventListener('DOMContentLoaded', () => {

    const formulario = document.querySelector('.formulario');

    if (!formulario) return;

    const boton = formulario.querySelector('button');

    const inputs = formulario.querySelectorAll('input');

    boton.disabled = true;

    inputs.forEach(input => {

        const error = document.createElement('small');

        error.style.color = 'red';

        input.parentNode.appendChild(error);

        input.addEventListener('input', () => {

            validarInput(input, error);

            validarFormulario();
        });
    });

    function validarInput(input, error) {

        let valido = true;

        // Campo vacío
        if (input.value.trim() === '') {

            valido = false;

            error.textContent = 'Campo obligatorio';
        }

        // Email
        else if (input.name === 'Email' &&
            !input.value.includes('@')) {

            valido = false;

            error.textContent = 'Email incorrecto';
        }

        // Teléfono
        else if (input.name === 'Telefono' &&
            input.value.length < 9) {

            valido = false;

            error.textContent = 'Telefono demasiado corto';
        }

        else {

            error.textContent = '';
        }

        // Colores
        if (valido) {

            input.style.border = '2px solid green';

        } else {

            input.style.border = '2px solid red';
        }

        return valido;
    }

    function validarFormulario() {

        let valido = true;

        inputs.forEach(input => {

            const error = input.parentNode.querySelector('small');

            if (!validarInput(input, error)) {

                valido = false;
            }
        });

        boton.disabled = !valido;
    }

});