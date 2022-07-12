# from django.test import TestCase
# from django.contrib.auth.models import User
# from virtual_agora.models import Post, Theme

# # Create your tests here.
# class TestCreatePost(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         test_theme = Theme.objects.create(name='happy')
#         test_user1 = User.objects.create_user(
#             username='testuser1',
#             password='12345'
#         )
#         test_post = Post.objects.create(
#             title='Test title',
#             description='Test description',
#             author= test_user1,
#             theme= test_theme.id,
#             status='draft',
#             slug = 'test-title',
#         )

#     def test_post_content(self):
#         post = Post.post_objects.get(id=1)
#         theme = Theme.objects.get(id=1)
#         title = f'{post.title}'
#         description = f'{post.description}'
#         author = f'{post.author}'
#         status = f'{post.status}'
#         self.assertEqual(author, 'testuser1')
#         # self.assertEqual(title, 'Test title')
#         # self.assertEqual(description, 'Test description')
#         # self.assertEqual(status, 'published')
#         # self.assertEqual(str(post),'Test title')
#         # self.assertEqual(str(theme),'happy')
