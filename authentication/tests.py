from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class TokenObtainPairViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('token_obtain_pair')
        self.username = 'testuser'
        self.password = 'testpass'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_token_obtain_pair(self):
        response = self.client.post(self.url, {'username': self.username, 'password': self.password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_refresh(self):
        token = RefreshToken.for_user(self.user)
        response = self.client.post(reverse('token_refresh'), {'refresh': str(token)}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)