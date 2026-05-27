document.addEventListener('DOMContentLoaded', () => {

    const formulario = document.querySelector('.formulario');
    if (!formulario) return;

    if (formulario.dataset.iniciado) return;
    formulario.dataset.iniciado = 'true';

    const boton = formulario.querySelector('button');
    const inputs = formulario.querySelectorAll('input');

    boton.disabled = true;


    inputs.forEach(input => {

        let siguiente = input.nextElementSibling;
        while (siguiente && siguiente.tagName === 'SMALL') {
            const aEliminar = siguiente;
            siguiente = siguiente.nextElementSibling;
            aEliminar.remove();
        }

        const error = document.createElement('small');
        error.className = 'error-mensaje';
        error.style.color = 'red';
        error.style.display = 'block';
        error.style.minHeight = '1em';
        error.setAttribute('aria-live', 'polite');

        input.insertAdjacentElement('afterend', error);
        input.errorElemento = error;
        input.touched = false;

        input.addEventListener('input', () => {
            input.touched = true;
            validarInput(input);
            actualizarBoton();
        });

        input.addEventListener('blur', () => {
            input.touched = true;
            validarInput(input);
            actualizarBoton();
        });
    });


    function validarInput(input) {
        const error = input.errorElemento;
        const valor = input.value.trim();
        let mensaje = '';

        if (valor === '') {
            mensaje = 'Campo obligatorio';
        } else {
            switch (input.name) {
                case 'DNI':
                    if (!/^\d{8}[A-Za-z]$/.test(valor))
                        mensaje = 'DNI incorrecto (ej: 12345678A)';
                    break;
                case 'Nombre':
                    if (valor.length < 2)
                        mensaje = 'Nombre demasiado corto';
                    break;
                case 'Apellido':
                    if (valor.length < 2)
                        mensaje = 'Apellido demasiado corto';
                    break;
                case 'Email':
                    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor))
                        mensaje = 'Email incorrecto';
                    break;
                case 'Telefono':
                    if (!/^\d{9}$/.test(valor))
                        mensaje = 'Teléfono incorrecto (9 dígitos)';
                    break;
            }
        }

        const valido = mensaje === '';

        if (input.touched) {
            error.textContent = mensaje;
            input.style.border = valido ? '2px solid green' : '2px solid red';
        }

        return valido;
    }


    function esValido(input) {
        const valor = input.value.trim();
        if (valor === '') return false;
        switch (input.name) {
            case 'DNI':     return /^\d{8}[A-Za-z]$/.test(valor);
            case 'Nombre':  return valor.length >= 2;
            case 'Apellido':return valor.length >= 2;
            case 'Email':   return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor);
            case 'Telefono':return /^\d{9}$/.test(valor);
            default:        return true;
        }
    }


    function actualizarBoton() {
        boton.disabled = ![...inputs].every(esValido);
    }


    boton.addEventListener('click', () => {


        inputs.forEach(input => {
            input.touched = true;
            validarInput(input);
        });


        if ([...inputs].every(esValido)) {
            console.log('Formulario enviado correctamente ✓');
 
        }
    });

});