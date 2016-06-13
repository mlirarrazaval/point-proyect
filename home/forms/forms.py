from django import forms
from ..models import *
from datetime import datetime, date
from .utils import *


class CreatePacientForm(forms.Form):

    nombres = forms.CharField(widget=forms.TextInput(attrs=NOMBRE_ATTRS),
                              error_messages=ERROR_REQ)
    apellido_paterno = forms.CharField(
        widget=forms.TextInput(attrs=APELLIDO_ATTRS),
        error_messages=ERROR_REQ)
    apellido_materno = forms.CharField(
        widget=forms.TextInput(attrs=APELLIDO_ATTRS),
        error_messages=ERROR_REQ)
    fecha = forms.CharField(widget=forms.TextInput(attrs=FECHA_ATTRS),
                            error_messages=ERROR_REQ)
    rut = forms.CharField(widget=forms.TextInput(attrs=RUT_ATTRS),
                          error_messages=ERROR_REQ)
    # direccion = forms.CharField(widget=forms.TextInput(attrs=DIRECCION_ATTRS),
    #                             error_messages=ERROR_REQ)
    email = forms.EmailField(widget=forms.EmailInput(attrs=EMAIL_ATTRS),
                             error_messages=ERROR_REQ)
    seguro = forms.CharField(widget=forms.TextInput(attrs=SEGURO_ATTRS),
                             error_messages=ERROR_REQ)
    telefono = forms.IntegerField(widget=forms.NumberInput(attrs=TELEFONO_ATTRS),
                                  error_messages=ERROR_TEL, max_value=999999999,
                                  min_value=100000000)
    ficha_medica = forms.CharField(widget=forms.Textarea(attrs=FICHA_ATTRS),
                                   error_messages=ERROR_REQ)

    def clean(self):
        cleaned_data = super().clean()
        if 'fecha' in cleaned_data:
            fecha = cleaned_data['fecha']
            try:
                cleaned_data['fecha'] = datetime.strptime(fecha, '%d/%m/%y')
            except ValueError:
                self.add_error('fecha', forms.ValidationError(
                    'Ingrese una fecha válida de formato DD/MM/AA.'))
        if 'rut' in cleaned_data:
            rut = cleaned_data['rut']
            verificacion, rut = verificar_limpiar_rut(rut)
            if not verificacion:
                self.add_error('rut', forms.ValidationError(
                    'Ingrese un RUT válido de la forma 12345678k.'))
            else:
                cleaned_data['rut'] = rut
            if Paciente.objects.filter(rut=rut):
                self.add_error('rut', forms.ValidationError(
                    'Un paciente con este RUT ya existe.'))

    def save(self):
        cleaned_data = super().clean()
        paciente = Paciente(nombres=cleaned_data['nombres'],
                            apellido_paterno=cleaned_data['apellido_paterno'],
                            apellido_materno=cleaned_data['apellido_materno'],
                            fecha_nacimiento=cleaned_data['fecha'].date(),
                            rut=cleaned_data['rut'],
                            seguro=cleaned_data['seguro'],
                            ranking=0,
                            ficha=cleaned_data['ficha_medica'],
                            telefono_contacto=cleaned_data['telefono'],
                            mail=cleaned_data['email'],
                            avisar_a='Relativo',
                            via_de_contacto='Mail')
        paciente.save()
        return paciente
