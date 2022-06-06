from django.test import TestCase
from .models import Url_Links
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import get_user_model
from accounts.models import Profile


class TestModels(TestCase):

    # Test default for new link is visible
    def test_visible_defaults_to_true(self):
        user1 = get_user_model().objects.create(username="foo",
                                                email="test@test.com",
                                                password="bar")
        link = Url_Links.objects.create(title='Test Title',
                                        link='http://www.rte.ie', user=user1)
        self.assertTrue(Url_Links.visible)

    # Test string method returns Link Title
    def test_link_string_method_returns_name(self):
        user1 = get_user_model().objects.create(username="foo",
                                                email="test@test.com",
                                                password="bar")
        link = Url_Links.objects.create(title='Test Title',
                                        link='http://www.rte.ie', user=user1)
        self.assertEqual(str(link), 'Test Title')
