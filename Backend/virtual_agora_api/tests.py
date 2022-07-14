from cgitb import reset
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
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
        self.testuser1 = User.objects.create_superuser(
            username='testuser1',
            password='12345'
        )

        self.client.login(username=self.testuser1.username, password='12345')

        data = {
            'title': 'Test title',
            'author': 1,
            'description': 'Test description'
        }
        url = reverse('virtual_agora_api:post_list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        client = APIClient()
        self.test_category = Theme.objects.create(name='happy')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='12345')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='12345')
        test_post = Post.objects.create(
            title='Post Title', description='Post Content', slug='post-title', author_id=1, status='published')

        client.login(username=self.testuser1.username,
                     password='12345')

        url = reverse(('virtual_agora_api:post_detail'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "title": "New",
                "author": 1,
                "description": "New",
                "status": "published"
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
