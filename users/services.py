from django.core.mail import send_mail
import abc
import smtplib
from email.mime.text import MIMEText

class EventHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, user):
        pass


class NotificationEmailSender(EventHandler):
    def update(self, user):
        email = user.email 
        msg = 'Alerta de login.Registramos um novo login em sua conta no EconomizAqui. Caso não tenha sido você, favor redefinir sua senha!'
        # self.notify(msg, email)

    def notify(self, texto, email):
        email_to = ['noreplayfiscae@gmail.com']
        subject = 'Login detectado'
        mensagem = MIMEText(texto)
        mensagem.set_charset('utf-8')
        mensagem['Subject'] = subject
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('noreplayfiscae@gmail.com', 'fiscaeunb')
        mail.sendmail('noreplayfiscae@gmail.com', email, mensagem.as_string())