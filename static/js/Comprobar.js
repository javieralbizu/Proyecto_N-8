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

        // DNI
        else if (
            input.name === 'DNI' &&
            !/^\d{8}[A-Za-z]$/.test(input.value)
        ) {

            valido = false;

            error.textContent = 'DNI incorrecto';
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
        else if (input.name === 'Telefono' &&
            input.value.length > 9) {

            valido = false;

            error.textContent = 'Telefono demasiado largo';
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