let tamanoContenido = 15;
let tamanoTitulo = 32;

async function comprobarLogin() {

    const parametros = new URLSearchParams(window.location.search);

    const token = parametros.get("token");


    if (!token) {

        let privado = document.getElementsByClassName("privado")
        for (let i = 0; i < privado.length; i++) {
            privado[i].style.display = "none";
        }
        return;
    }

    fetch("/comprobar/", {
        headers: {
            "Authorization": "Bearer " + token
        }
    })
        .then(respuesta => {
            if (!respuesta.ok) {
                let privado = document.getElementsByClassName("privado");
                for (let i = 0; i < privado.length; i++) {
                    privado[i].style.display = "none";
                }
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
}
comprobarLogin();

const formulario = document.querySelector('form:not(.formbuscador)');

if (formulario) {
    formulario.onsubmit = function () {
        alert("Formulario enviado correctamente");
    };
}

function aumento() {
    if (tamanoContenido < 30) {
        tamanoContenido += 1;
        tamanoTitulo += 1;
        aplicarTamano();
    }
}

function disminuir() {
    if (tamanoContenido > 9) {
        tamanoContenido -= 1;
        tamanoTitulo -= 1;
        aplicarTamano();
    }
}

const elementos = document.querySelectorAll('p,th,td,a,button,label');
const titulos = document.querySelectorAll('h1');

function aplicarTamano() {

    elementos.forEach(elemento => {
        elemento.style.fontSize = tamanoContenido + "px";
    });

    titulos.forEach(t => {
        t.style.fontSize = tamanoTitulo + "px";
    })
}
