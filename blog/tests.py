from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuração dos dados de teste uma vez para todos os métodos de teste
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()

        test_post = Post.objects.create(author=test_user, title='Test Post', text='This is a test post.')
        test_post.save()

    def test_publish_method(self):
        post = Post.objects.get(id=1)
        post.publish()
        self.assertIsNotNone(post.published_date)
        self.assertTrue(post.published_date, timezone.now())

    def test_str_method(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), 'Test Post')
