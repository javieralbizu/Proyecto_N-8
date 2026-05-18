function conectar() {

    const usuario = document.getElementById("user").value;
    const clave = document.getElementById("pass").value;

    if (!usuario || !clave) {
        alert("Por favor, rellena todos los campos");
        return;
    }

    fetch("http://127.0.0.1:8000/api/token/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: usuario,
            password: clave
        })
    })
        .then(respuesta => {
            return respuesta.json().then(datos => {
                return { ok: respuesta.ok, datos: datos };
            });
        })
        .then(resultado => {
            if (resultado.ok) {
                const token = resultado.datos.access;
                window.location.href = "http://127.0.0.1:8000/?token=" + token;
            } else {
                alert("Usuario o contraseña incorrectos");
            }
        })
        .catch(error => {
            console.error("Error de red:", error);
            alert("Error de conexión con el servidor");
        });
}