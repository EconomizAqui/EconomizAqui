from django.core.mail import send_mail
import abc


class EventHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, user):
        pass


class NotificationEmailSender(EventHandler):
    def update(self, user):
        email = user.email
        
        sent = send_mail(
            'Alerta de login',
            'Registramos um novo login em sua conta no EconomizAqui. '
            + 'Caso não tenha sido você, favor redefinir sua senha.',
            'economizaqui@email.com',
            [email],
            fail_silently=False,
        )

        if (sent):
            print('Email de alerta de login enviado')

