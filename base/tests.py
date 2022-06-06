from django.urls import reverse

from django.test import TestCase
from .models import User, Task


class TestUser(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('test_user', email=None, password='testpass')

    def test_get_user(self):
        user = User.objects.get(username='test_user')
        self.assertTrue(user.check_password('testpass'))

    def test_login(self):
        login = self.client.login(username='test_user', password='testpass')
        self.client.logout()

    def test_main_view(self):
        response = self.client.get(f'')
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(f'/login')
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        response = self.client.get(f'/logout')
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(f'/register')
        self.assertEqual(response.status_code, 200)

    def test_task_create_view(self):
        response = self.client.get(f'/task-create')
        self.assertEqual(response.status_code, 200)
