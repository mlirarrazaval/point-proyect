from django import forms
from .models import *
from datetime import date


class CreatePacientForm(forms.Form):

	nombre = forms.CharField()
	apellido = forms.CharField()
	rut = forms.CharField()
	fecha = forms.CharField()

	def save(self):
		cleaned_data = super().clean()
		dates = cleaned_data['fecha']
		f = dates.split('-')
		dates = date(year=f[0], month=f[1], day=f[2])
		p = Paciente(rut=cleaned_data['rut'],
					 nombres=cleaned_data['nombre'],
					 apellido_paterno=cleaned_data['apellido'],
					 fecha_nacimiento=dates,
					 apellido_materno='Bulnes',
					 seguro='Fonasa',
					 ranking=9.9,
					 ficha='a',
					 telefono_contacto='22145555',
					 mail='a@b.com',
					 avisar_a='papa',
					 via_de_contacto='SMS'
					 )
		p.save()
		return p



	
	