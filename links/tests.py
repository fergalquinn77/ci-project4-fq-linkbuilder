from django.test import TestCase


class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertAlmostEqual(response.status.code, 200)
