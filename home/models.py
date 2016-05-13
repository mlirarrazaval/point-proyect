from django.db import models

SEGUROS = [('Fonasa', 'Fonasa')]
VIAS = [('Mail', 'Mail'), ('Llamada', 'Llamada'), ('SMS', 'SMS')]
ESTADOS = [('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada'), ('Desconocido', 'Desconocido')]

class Paciente(models.Model):
	nombres = models.CharField(max_length=50)
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	rut = models.CharField(max_length=10)
	seguro = models.CharField(choices=SEGUROS, max_length=20)
	ranking = models.FloatField()
	ficha = models.CharField(max_length=500)# se puede poner un archivo?
	telefono_contacto = models.CharField(max_length=10)
	mail = models.CharField(max_length=10)
	avisar_a = models.CharField(max_length=50)# puede ser dos cosas? numero y nombre?
	via_de_contacto = models.CharField(choices=VIAS, max_length=20)

	def __str__(self):
		return self.nombres + ' ' + self.apellido_paterno

class Doctor(models.Model):
	nombres = models.CharField(max_length=50)
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	especialidad = models.CharField(max_length=50)
	horario_atencion = models.CharField(max_length=50)

class Consulta(models.Model):
	paciente = models.CharField(max_length=50)
	fecha_consulta = models.DateTimeField()
	doctor = models.CharField(max_length=50)
	estado = models.CharField(choices=ESTADOS, max_length=20)

	


