from django.test import TestCase, Client
from .models import CustomUser
from django.core import mail
import os, shutil
import glob


class NotificationEmailSenderTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = CustomUser.objects.create_user(username='test',
                                                    password='abc1234',
                                                    name='Teste',
                                                    email='teste@email.com')
        self.user.save()

    def test_email_sent(self):
        self.c.post(
            '/users/login/',
            {'username': 'test', 'password': 'abc1234'},
            follow=True
            )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Alerta de login')
