import re


# USER_FIELD_ATTRS = {'class': 'form-control border-input'}
NOMBRE_ATTRS = {'placeholder': 'Ingresar nombre o nombres',
                'class': 'form-control border-input'}
APELLIDO_ATTRS = {'placeholder': 'Ingresar apellido',
                  'class': 'form-control border-input'}
FECHA_ATTRS = {'placeholder': 'DD/MM/AA',
               'class': 'form-control border-input'}
RUT_ATTRS = {'placeholder': '12345678-k',
             'class': 'form-control border-input'}
DIRECCION_ATTRS = {'placeholder': 'Ingresar direccion',
                   'class': 'form-control border-input'}
EMAIL_ATTRS = {'placeholder': 'paciente@point.cl',
               'class': 'form-control border-input'}
SEGURO_ATTRS = {'placeholder': 'Seguro médico',
                'class': 'form-control border-input'}
TELEFONO_ATTRS = {'placeholder': '999999999',
                  'class': 'form-control border-input'}
FICHA_ATTRS = {'placeholder': 'Grupo Sanguíneo:\nEnfermedades Crónicas:\nAlergia a medicamentos:\nOperaciones realizadas:',
               'class': 'form-control border-input', 'rows': 5}
ERROR_REQ = {'required': 'Este campo es requerido.'}
ERROR_TEL = {'max_value': 'El número debe tener 9 dígitos.',
             'min_value': 'El número debe tener 9 dígitos.',
             'required': 'Este campo es requerido.'}


def regex_rut(rut):
    return bool(re.match(
        '^(\d{1,8}|\d{1,2}(\.\d{3}){2}|\d{1,3}(\.\d{3}))(\-)?([\dkK])$', rut))


def digito_verificador_valido(rut):
    multiplicadores = [3, 2, 7, 6, 5, 4, 3, 2]
    rut = rut.replace('.', '', 2).upper()
    digito_enviado = rut[-1]
    rut = rut.replace('-', '', -1)[:-1].zfill(8)
    suma = sum(int(rut[_]) * multiplicadores[_] for _ in range(8))
    dig = 11 - suma % 11
    digito_esperado = 'K' if dig == 10 else 0 if dig == 11 else dig
    return digito_enviado == str(digito_esperado), rut


def verificar_limpiar_rut(rut):
    if regex_rut(rut):
        return digito_verificador_valido(rut)
    return False, ''
