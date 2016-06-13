from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseForbidden
from .forms import CreatePacientForm
from .models import *
from datetime import datetime, timedelta
import json


def home(request):
    return render(request, 'dashboard.html', {})


def user(request):
    form = CreatePacientForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {})
    return render(request, 'new_pacient.html', {'form': form})


def waitlist(request):
    return render(request, 'table.html', {})


def appointments(request):
    return render(request, 'tomadehoras.html', {})


def calendar(request):
    consultas_espera = Consulta.objects.filter(fecha__gt=datetime.now())
    pacientes_espera = Paciente.objects.all().exclude(
        id__in=consultas_espera.values_list('paciente__id', flat=True))
    doctores = Doctor.objects.all()
    data = {'pacientes_espera': pacientes_espera,
            'doctores': doctores,
            'consultas': Consulta.objects.all()}
    return render(request, 'calendario.html', data)


# INICIO LISTAS (POR BORRAR)

def cardiologia(request):
    return render(request, 'listaesperacardiologia.html', {})


def traumatologia(request):
    return render(request, 'listaesperatraumatologia.html', {})


def urologia(request):
    return render(request, 'listaesperaurologia.html', {})


def todas(request):
    return render(request, 'todaslaslistas.html', {})


# TÉRMINO LISTAS


# ###########################
# #########  API  ###########
# ###########################


@require_http_methods(["POST"])
def create_appointment(request):
    if 'pacient' in request.POST and 'doctor' in request.POST:
        data = {'error': 'error'}
        paciente = Paciente.objects.filter(id=request.POST['pacient'])
        doctor = Doctor.objects.filter(id=request.POST['doctor'])
        if paciente and doctor:
            paciente = paciente.get()
            doctor = doctor.get()
            fecha = datetime.strptime(request.POST['date'],
                                      '%a, %d %b %Y %H:%M:%S GMT')
            duracion = timedelta(minutes=int(request.POST['duration']))
            consulta = Consulta(paciente=paciente, fecha=fecha,
                                duracion=duracion, doctor=doctor,
                                estado='Desconocido')
            consulta.save()
            data = {'id': consulta.id, 'title': consulta.titulo,
                    'description': consulta.descripcion}
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponseForbidden()


@require_http_methods(["POST"])
def enviar_recordatorios(request):
    # manana = datetime.now().date() + timedelta(days=1)
    # desde = datetime.combine(manana, datetime.min.time())
    # hasta = datetime.combine(manana, datetime.max.time())
    desde = datetime.now()
    hasta = datetime.now() + timedelta(hours=30)
    consultas = Consulta.objects.filter(fecha__gt=desde,
                                        fecha__lt=hasta)
    errores = []
    for consulta in consultas:
        if not consulta.enviar_recordatorio():
            errores.append(consulta)
    if errores:
        nombres = ', '.join([str(i.paciente) for i in errores])
        data = {'error': 'No se pudieron enviar los mensajes a: ' + nombres}
    else:
        data = {'info': 'Se enviaron satisfactoriamente %d mails' % len(
            consultas)}
    return HttpResponse(json.dumps(data), content_type="application/json")
