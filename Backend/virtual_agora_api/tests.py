from cgitb import reset
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from virtual_agora.models import Post, Theme
from django.contrib.auth.models import User

# Create your tests here.


class PostTests(APITestCase):
    def test_view_posts(self):
        url = reverse('virtual_agora_api:post_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.test_theme = Theme.objects.create(name='happy')
        self.testuser1 = User.objects.create_user(
            username='testuser1',
            password='12345'
        )

        data = {
            'title': 'Test title',
            'author': 1,
            'description': 'Test description'
        }
        url = reverse('virtual_agora_api:post_list')
        response = self.client.post(url, data, format='json') 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
