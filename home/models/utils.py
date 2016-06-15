from django.template.loader import render_to_string
import sendgrid


def mail_recordatorio(consulta):
    paciente = consulta.paciente
    try:
        sg_api_key = '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'
        sg = sendgrid.SendGridClient(sg_api_key)
        message = sendgrid.Mail()

        link = 'http://point.cl/'
        name = paciente.nombre_completo
        html_mail = render_to_string('mails/recordatorio.html',
                                     {'name': name, 'link': link,
                                      'consulta': consulta})

        message.set_from("recordatorios@point.cl")
        message.set_subject("Recuerda tu hora de mañana!")
        message.set_text(" ")
        message.set_html(html_mail)
        message.add_to(paciente.mail)

        status, msg = sg.send(message)
        print(msg, status)
        return True
    except Exception as err:
        print('Error al enviar el recordatorio a %s' % paciente.mail)
        print(err)
        return False
