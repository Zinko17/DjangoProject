from django.test import TestCase
from django.urls import reverse

from .models import User, Profile


class RegisterTest(TestCase):

    def setUp(self) -> None:
        self.url = reverse('register')

    def test_register_ok(self):
        data = {
            'name': 'sdfla;f',
            'age': 22,
            'email': 'jjj@gmail.com',
            'username': '788',
            'password1': 'django123',
            'password2': 'django123'
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, 200)

    def test_register_notok_age(self):
        data = {
            'name': 'sdfla;f',
            'email': 'jjj@gmail.com',
            'username': '788',
            'password1': 'django123',
            'password2': 'django123'
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='age', errors='This field is required.', form='form')

    def test_register_notok_name(self):
        data = {
            'age': 18,
            'email': 'jjj@gmail.com',
            'username': '788',
            'password1': 'django123',
            'password2': 'django123'
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='name', errors='This field is required.', form='form')

    def test_register_notok_username(self):
        data = {
            'name': 'mfnlanf',
            'age': 18,
            'email': 'jjj@gmail.com',
            'password1': 'django123',
            'password2': 'django123'
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='username', errors='This field is required.', form='form')

    def test_register_notok_email(self):
        data = {
            'name': 'mfnlanf',
            'age': 18,
            'username': 'sfasd',
            'password1': 'django123',
            'password2': 'django123'
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='email', errors='This field is required.', form='form')

    def test_register_notok_password1(self):
        data = {
            'name': 'mfnlanf',
            'age': 18,
            'username': 'sfasd',
            'email': 'sfss@gmail.com',
            'password2': 'django123'
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='password1', errors='This field is required.', form='form')

    def test_register_notok_password2(self):
        data = {
            'name': 'mfnlanf',
            'age': 18,
            'username': 'sfasd',
            'email': 'sfss@gmail.com',
            'password1': 'django123'
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='password2', errors='This field is required.', form='form')

    def test_register_template(self):
        data = {
            'name': 'sdfla;f',
            'age': 22,
            'email': 'jjj@gmail.com',
            'username': '788',
            'password1': 'django123',
            'password2': 'django123'
        }
        self.response = self.client.post(self.url, data)
        self.assertTemplateUsed(self.response, 'register.html')
