from django.test import TestCase
from .models import Url_Links
from django.contrib.auth import get_user_model

class TestViews(TestCase):

# Test Main Index Page
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/learn.html')

    def test_external_page(self):
        test_user = get_user_model().objects.create(username="foo", email="test@test.com", password="bar")
        response = self.client.get((f'/user/{test_user.username}'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/index_external.html')