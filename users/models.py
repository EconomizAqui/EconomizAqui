from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in
from .services import NotificationEmailSender


class CustomUser(AbstractUser):
    def __str__(self):
        return self.email

    name = models.CharField(max_length=100, blank=False)
    pontos = models.IntegerField(default=0)
    
    event_handlers = []

    def attach(self, event_handler):
        if event_handler not in self.event_handlers:
            self.event_handlers.append(event_handler)

    def detach(self, event_handler):
        try:
            self.event_handlers.remove(event_handler)
        except ValueError:
            pass

    def notify(user, **kwarg):
        event_handler = NotificationEmailSender()
        user.attach(event_handler)
        
        for event_handler in user.event_handlers:
            event_handler.update(user)

    user_logged_in.connect(notify)
