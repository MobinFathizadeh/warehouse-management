from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import User, Role


class LoginTestCase(TestCase):
    def setUp(self):
        self.role  =Role.objects.create(name='warehouse_manager', description='مدیر انبار')
        self.user = User.objects.create_user(
            username= 'testuser',
            password= 'TestPass123',
            role = self.role
        )
        self.client = APIClient()



    def test_login__with_correct_credentials(self):
        response = self.client.post('/api/auth/login/',{
            'username': 'testuser',
            'password': 'TestPass123',
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


    def test_login_with_wrong_password(self):
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'WrongPassword',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
