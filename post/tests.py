from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import *
# Create your tests here.


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Post.objects.create(
            author = test_user,
            title = 'Title of Blog',
            body = 'Words about the blog'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)

        self.assertEqual(str(post.author), 'tester')
        self.assertEqual(post.title, 'Title of Blog')
        self.assertEqual(post.body, 'Words about the blog')    
        