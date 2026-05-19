from django.shortcuts import render , redirect, get_object_or_404
from .forms import IntervencionForm
from .models import Intervencion
from django.conf import settings
from django.core.mail import send_mail

def CargarTablaIncidencias(request):
    token = request.GET.get("token")
    intervenciones = Intervencion.objects.all()
    return render(request, 'Incidencias/Tabla.html',{'Incidencias':intervenciones, "jwt_token":token} )

def NuevaIncidencia(request, id=None):
    token = request.GET.get("token")
    if id:
        incidencia = get_object_or_404(Intervencion,id=id)
    else:
        incidencia= None

    if request.method == 'POST':
        form = IntervencionForm(request.POST, instance=incidencia)
        if form.is_valid():
            incidencia= form.save()
            MandarCorreo(incidencia)
            return redirect(f"/Incidencias/?token={token}")
            
    else: 
        form = IntervencionForm(instance=incidencia)

    return render(request, 'Incidencias/NuevaIncidencia.html', {'form': form, 'jwt_token': token})

def EliminarIncidencia(request, id):
    token = request.GET.get("token")
    incidencia = get_object_or_404(Intervencion,id=id)
    incidencia.delete()
    return redirect(f"/Incidencias/?token={token}")

    
def MandarCorreo(incidencia):
    asunto = "Intervencion Nueva"
    mensaje = f"""

    Se ha registrado una nueva incidencia con los siguientes detalles:

    Codigo: {incidencia.Codigo}
    Fecha Apertura: {incidencia.FechaApertura}
    Fecha Cierre: {incidencia.FechaCierre}
    Tipo Intervencion : {incidencia.TipoIntervencion}
    Descripcion : {incidencia.Descripcion}
    Tecnico Asiganado : {incidencia.TecnicoAsignado}
    Elemento : {incidencia.ActivoAsignado}
    
    Por favor, revise el panel de administración para más detalles.
    """
    
    email_desde = settings.EMAIL_HOST_USER
    emails_destino = [settings.EMAIL_HOST_USER]
    
    try:
        send_mail(
            asunto,
            mensaje,
            email_desde,
            recipient_list=emails_destino,
            fail_silently=False,
        )
        print("mensaje enviado")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")