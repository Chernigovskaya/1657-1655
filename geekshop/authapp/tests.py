from django.conf import settings
from django.test import TestCase
from authapp.models import User
from django.test.client import Client


class UserTestCase(TestCase):

    def setUp(self) -> None:
        self.username = 'django'
        self.email = 'django@mail.ru'
        self.password = 'Geekshop_@1234'

        self.new_user_data = {
            'username': 'django1',
            'first_name': 'django1',
            'last_name': 'django1',
            'email': 'django1@mail.ru',
            'password1': 'Geekshop_@1',
            'password2': 'Geekshop_@1',
            'age': 25,
        }

        self.user = User.objects.create_superuser(self.username, self.email,
                                                  self.password)
        self.client = Client()

    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/authapp/profile/')
        self.assertEqual(response.status_code, 302)

        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/authapp/profile/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.post('/authapp/register/', data=self.new_user_data)

        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username=self.new_user_data['username'])

        activation_url = f'{settings.DOMAIN_NAME}/authapp/verify/' \
                         f'{user.email}/{user.activation_key}/'
        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(user.is_active)
        user.refresh_from_db()
        self.assertTrue(user.is_active)

    def tearDown(self) -> None:
        pass
