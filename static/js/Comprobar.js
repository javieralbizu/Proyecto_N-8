document.addEventListener('DOMContentLoaded', () => {

    const formulario = document.querySelector('.formulario');
    if (!formulario) return;

    if (formulario.dataset.iniciado) return;
    formulario.dataset.iniciado = 'true';

    const boton = formulario.querySelector('button');
    const inputs = formulario.querySelectorAll('input, select, textarea');

    boton.disabled = true;

    // ─── Inicialización ──────────────────────────────────────────────────────
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

    // ─── Validación individual (visual) ─────────────────────────────────────
    function validarCampo(campo) {
        const error = campo.errorElemento;
        const valor = campo.value.trim();
        const nombre = campo.name;
        let mensaje = '';

        if (campo.tagName === 'SELECT') {
            if (!valor || valor === '' || valor === '0') {
                mensaje = 'Selecciona una opción';
            }
        }

        else if (valor === '') {
            mensaje = 'Campo obligatorio';
        }

        else {
            switch (nombre) {
                // ── Formulario Técnico ────────────────────────────────────
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

                // ── Formulario Intervención ───────────────────────────────
                case 'Codigo':
                    if (!/^\d+$/.test(valor))
                        mensaje = 'El código debe ser numérico';
                    else if (parseInt(valor) <= 0)
                        mensaje = 'El código debe ser mayor que 0';
                    break;
                case 'FechaApertura':
                    if (!esFechaValida(valor))
                        mensaje = 'Fecha de apertura inválida';
                    break;
                case 'FechaCierre': {
                    if (!esFechaValida(valor)) {
                        mensaje = 'Fecha de cierre inválida';
                    } else {
                        const apertura = formulario.querySelector('[name="FechaApertura"]');
                        if (apertura && apertura.value && valor < apertura.value)
                            mensaje = 'No puede ser anterior a la fecha de apertura';
                    }
                    break;
                }
                case 'TipoIntervencion':
                    if (valor.length < 3)
                        mensaje = 'Demasiado corto (mín. 3 caracteres)';
                    break;
                case 'Descripcion':
                    if (valor.length < 5)
                        mensaje = 'Demasiado corta (mín. 5 caracteres)';
                    break;
            }
        }

        const valido = mensaje === '';

        if (campo.touched) {
            error.textContent = mensaje;
            campo.style.border = valido ? '2px solid green' : '2px solid red';
        }

        return valido;
    }

    // ─── Validación pura (sin tocar el DOM) ──────────────────────────────────
    function esValido(campo) {
        const valor = campo.value.trim();
        const nombre = campo.name;

        if (campo.tagName === 'SELECT')
            return valor && valor !== '' && valor !== '0';

        if (valor === '') return false;

        switch (nombre) {
            // ── Formulario Técnico ────────────────────────────────────────
            case 'DNI':     return /^\d{8}[A-Za-z]$/.test(valor);
            case 'Nombre':  return valor.length >= 2;
            case 'Apellido':return valor.length >= 2;
            case 'Email':   return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor);
            case 'Telefono':return /^\d{9}$/.test(valor);

            // ── Formulario Intervención ───────────────────────────────────
            case 'Codigo':  return /^\d+$/.test(valor) && parseInt(valor) > 0;
            case 'FechaApertura': return esFechaValida(valor);
            case 'FechaCierre': {
                if (!esFechaValida(valor)) return false;
                const apertura = formulario.querySelector('[name="FechaApertura"]');
                if (apertura && apertura.value && valor < apertura.value) return false;
                return true;
            }
            case 'TipoIntervencion': return valor.length >= 3;
            case 'Descripcion':      return valor.length >= 5;

            default: return true;
        }
    }

    // ─── Helper fecha ────────────────────────────────────────────────────────
    function esFechaValida(valor) {
        if (!valor) return false;
        return !isNaN(new Date(valor).getTime());
    }

    // ─── Actualizar botón ────────────────────────────────────────────────────
    function actualizarBoton() {
        boton.disabled = ![...inputs].every(esValido);
    }

    // Revalidar FechaCierre si cambia FechaApertura
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

    // ─── Submit ──────────────────────────────────────────────────────────────
    boton.addEventListener('click', () => {

        inputs.forEach(campo => {
            campo.touched = true;
            validarCampo(campo);
        });

        if ([...inputs].every(esValido)) {
            console.log('Formulario enviado correctamente ✓');
            // formulario.submit();
        }
    });

});