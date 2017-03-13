from django.test import TestCase
from .models import Post

# Create your tests here.

class PostTests(TestCase):

    def test_stir(self):
        test_title = Post(title='My Latest Blog Post')
        self.assertEqual(str(test_title),
                         'My Latest Blog Post')