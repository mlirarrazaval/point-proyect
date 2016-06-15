from django.template.loader import render_to_string
import sendgrid


def mail_recordatorio(consulta):
    paciente = consulta.paciente
    try:
        sg_api_key = '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'
        print(1)
        sg = sendgrid.SendGridClient(sg_api_key)
        print(2)
        message = sendgrid.Mail()
        print(3)
        link = 'http://point.cl/'
        name = paciente.nombre_completo
        print(4)
        html_mail = render_to_string('mails/recordatorio.html',
                                     {'name': name, 'link': link,
                                      'consulta': consulta})
        print(5)
        message.set_from("recordatorios@point.cl")
        print(6)
        message.set_subject("Recuerda tu hora de mañana!")
        print(7)
        message.set_text(" ")
        print(8)
        message.set_html(html_mail)
        print(9)
        message.add_to(paciente.mail)
        print(10)
        status, msg = sg.send(message)
        print(11)
        print(msg, status)
        print(12)
        return True
    except:
        print('Error al enviar el recordatorio a %s' % paciente.mail)
        return False
