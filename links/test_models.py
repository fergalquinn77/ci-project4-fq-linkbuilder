from django.test import TestCase
from .models import Url_Links
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import get_user_model
from accounts.models import Profile

class TestModels(TestCase):
    
    def test_visible_defaults_to_true(self):
        user1 = get_user_model().objects.create(username="foo", email="test@test.com", password="bar")
        link = Url_Links.objects.create(title='Test Title', link='http://www.rte.ie', user=user1)
        self.assertTrue(Url_Links.visible)

    # def test_link_string_method_returns_name(self):
    #     user1=AnonymousUser()
    #     link = Url_Links.objects.create(title='Test Title', link='http://www.rte.ie', user=user1.user)
    #     item = Url_Links.objects.create_user(title='Test Title',link='http://www.rte.ie', user=self.user)
    #     self.assertEqual(str(item), 'Test Title')