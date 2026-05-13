function conectar() {
    const usuario = document.getElementById('user').value;
    const clave = document.getElementById('pass').value;

    fetch('http://127.0.0.1:8000/api/token/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: usuario, password: clave })
    })
    .then(respuesta => {
        if (respuesta.ok) {
            return respuesta.json(); 
        } else {
            throw new Error("Usuario o Contraseña incorrectos.");
        }
    })
    .then(datos => {
        localStorage.setItem('token_acceso', datos.access);
        localStorage.setItem('token_refresh', datos.refresh);

        alert("¡Éxito! Token guardado.");
        window.location.href = "http://127.0.0.1:8000";
    })
    .catch(error => {
        alert(error.message);
        console.error("Error de conexión:", error);
    });
}