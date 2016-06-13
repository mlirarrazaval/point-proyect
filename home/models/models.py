from datetime import datetime, timedelta
from django.db import models
from .utils import mail_recordatorio


SEGUROS = [('Fonasa', 'Fonasa')]
VIAS = [('Mail', 'Mail'), ('Llamada', 'Llamada'), ('SMS', 'SMS')]
ESTADOS = [('Confirmada', 'Confirmada'),
           ('Cancelada', 'Cancelada'),
           ('Desconocido', 'Desconocido')]


class Paciente(models.Model):
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    rut = models.CharField(max_length=10)
    seguro = models.CharField(choices=SEGUROS, max_length=20)
    ranking = models.FloatField()
    ficha = models.CharField(max_length=500)  # se puede poner un archivo?
    telefono_contacto = models.CharField(max_length=10)
    mail = models.EmailField(max_length=10)
    # puede ser dos cosas? numero y nombre?
    avisar_a = models.CharField(max_length=50)
    via_de_contacto = models.CharField(choices=VIAS, max_length=20)

    def __str__(self):
        return self.nombres + ' ' + self.apellido_paterno

    def nombre_completo(self):
        return '%s %s %s' % (self.nombres, self.apellido_paterno,
                             self.apellido_materno)


class Doctor(models.Model):
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    horario_atencion = models.CharField(max_length=50)

    def nombre_completo(self):
        return '%s %s %s' % (self.nombres, self.apellido_paterno,
                             self.apellido_materno)

    def __str__(self):
        return self.nombres + ' ' + self.apellido_paterno


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateTimeField()
    duracion = models.DurationField(default=timedelta(minutes=60))
    doctor = models.ForeignKey(Doctor)
    estado = models.CharField(choices=ESTADOS, max_length=20)

    @property
    def titulo(self):
        return '%s - %s' % (self.paciente, self.doctor)

    @property
    def descripcion(self):
        return self.paciente.mail

    @property
    def fecha_termino(self):
        return self.fecha + self.duracion

    def enviar_recordatorio(self):
        return mail_recordatorio(self)

    def __str__(self):
        fecha = self.fecha.strftime('%d-%m-%y %H:%M')
        return '%s %s con %s' % (self.paciente, fecha, self.doctor)
