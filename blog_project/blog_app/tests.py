from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):

    def setup(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email="test@gmail.com",
            password="secret",
        )

        self.post = Post.objects.create(
            title="normal title",
            body="normal body content",
            author=self.user,
        )

    def test_string_representation(self):
        post=Post("normal title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'normal title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'normal body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'normal body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')

        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'normal title')
        self.assertTemplateUsed(response, 'post_detail.html')
