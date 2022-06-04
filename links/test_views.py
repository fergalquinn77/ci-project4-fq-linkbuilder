from django.test import TestCase
from .models import Url_Links

class TestViews(TestCase):

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/learn.html')