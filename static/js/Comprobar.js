
document.addEventListener('DOMContentLoaded', () => {

    const formulario = document.querySelector('.formulario');
    if (!formulario) return;

    if (formulario.dataset.iniciado) return;
    formulario.dataset.iniciado = 'true';

    const boton = formulario.querySelector('button');
    const inputs = formulario.querySelectorAll('input, select, textarea');

    boton.disabled = true;

    inputs.forEach(campo => {

        let siguiente = campo.nextElementSibling;
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

        campo.insertAdjacentElement('afterend', error);
        campo.errorElemento = error;
        campo.touched = false;

        const evento = campo.tagName === 'SELECT' ? 'change' : 'input';

        campo.addEventListener(evento, () => {
            campo.touched = true;
            validarCampo(campo);
            actualizarBoton();
        });

        campo.addEventListener('blur', () => {
            campo.touched = true;
            validarCampo(campo);
            actualizarBoton();
        });
    });

    function esFechaValida(valor) {
        if (!valor) return false;
        return !isNaN(new Date(valor).getTime());
    }

    function obtenerError(campo) {
        const valor = campo.value.trim();
        const nombre = campo.name;

        if (campo.tagName === 'SELECT') {
            return (!valor || valor === '' || valor === '0') ? 'Selecciona una opción' : '';
        }

        if (valor === '') return 'Campo obligatorio';

        switch (nombre) {
            case 'DNI':
                return /^\d{8}[A-Za-z]$/.test(valor) ? '' : 'DNI incorrecto (ej: 12345678A)';
            case 'Nombre':
                return valor.length >= 2 ? '' : 'Nombre demasiado corto';
            case 'Apellido':
                return valor.length >= 2 ? '' : 'Apellido demasiado corto';
            case 'Email':
                return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor) ? '' : 'Email incorrecto';
            case 'Telefono':
                return /^\d{9}$/.test(valor) ? '' : 'Teléfono incorrecto (9 dígitos)';

            case 'Codigo':
                if (!/^\d+$/.test(valor)) return 'El código debe ser numérico';
                if (parseInt(valor) <= 0)  return 'El código debe ser mayor que 0';
                return '';
            case 'FechaApertura':
                return esFechaValida(valor) ? '' : 'Fecha de apertura inválida';
            case 'FechaCierre': {
                if (!esFechaValida(valor)) return 'Fecha de cierre inválida';
                const apertura = formulario.querySelector('[name="FechaApertura"]');
                if (apertura && apertura.value && valor < apertura.value)
                    return 'No puede ser anterior a la fecha de apertura';
                return '';
            }
            case 'TipoIntervencion':
                return valor.length >= 3 ? '' : 'Demasiado corto (mín. 3 caracteres)';
            case 'Descripcion':
                return valor.length >= 5 ? '' : 'Demasiado corta (mín. 5 caracteres)';

            default: return '';
        }
    }

    function validarCampo(campo) {
        const mensaje = obtenerError(campo);
        const valido = mensaje === '';

        if (campo.touched) {
            campo.errorElemento.textContent = mensaje;
            campo.style.border = valido ? '2px solid green' : '2px solid red';
        }

        return valido;
    }

    function esValido(campo) {
        return obtenerError(campo) === '';
    }

    function actualizarBoton() {
        boton.disabled = ![...inputs].every(esValido);
    }

    const fechaApertura = formulario.querySelector('[name="FechaApertura"]');
    const fechaCierre   = formulario.querySelector('[name="FechaCierre"]');
    if (fechaApertura && fechaCierre) {
        fechaApertura.addEventListener('change', () => {
            if (fechaCierre.touched) {
                validarCampo(fechaCierre);
                actualizarBoton();
            }
        });
    }

    boton.addEventListener('click', () => {

        inputs.forEach(campo => {
            campo.touched = true;
            validarCampo(campo);
        });

        if ([...inputs].every(esValido)) {
            console.log('Formulario enviado correctamente ✓');
        }
    });

});