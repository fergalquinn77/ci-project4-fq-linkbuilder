from django.test import TestCase
from .models import Url_Links
from django.contrib.auth import get_user_model
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse

class TestViews(TestCase):

# Test Main Index Page
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/learn.html')

# Test External View Page
    def test_external_page(self):
        test_user = get_user_model().objects.create(username="foo", email="test@test.com", password="bar")
        response = self.client.get(f'/user/{test_user.username}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/index_external.html')

#Test Add Link Page
    def test_add_link_page(self):
        user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
        self.client.login(username='foo', password='bar')
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/add_item.html')

# #Test Edit Link Page
#     def test_add_link_page(self):
#         user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
#         self.client.login(username='foo', password='bar')
#         response = self.client.get('/edit/')
#         self.assertEqual(response.status_code, 200)