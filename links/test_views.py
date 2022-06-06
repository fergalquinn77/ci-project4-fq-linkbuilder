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

#Test Edit Link Page
    def test_edit_link_page(self):
        user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
        self.client.login(username='foo', password='bar')
        link = Url_Links.objects.create(title='Test Title', link='http://www.rte.ie', user=user)
        response = self.client.get(f'/edit/{link.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/edit_item.html')

#Test Delete Link Page
    def test_delete_link_page(self):
        user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
        self.client.login(username='foo', password='bar')
        link = Url_Links.objects.create(title='Test Title', link='http://www.rte.ie', user=user)
        response = self.client.get(f'/delete/{link.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/confirm_delete.html')

#Test Can Edit Link
    def test_can_edit_link_page(self):
        user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
        self.client.login(username='foo', password='bar')
        link = Url_Links.objects.create(title='Test Title', link='http://www.rte.ie', user=user)
        response = self.client.post(f'/edit/{link.id}/', {'title':'Changed Title', 'link':'http://www.rte.ie'})
        updated_link = Url_Links.objects.get(id=link.id)
        self.assertEqual(updated_link.title, 'Changed Title')

#Test Can Delete Link
    def test_delete_link(self):
        user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
        self.client.login(username='foo', password='bar')
        link = Url_Links.objects.create(title='Test Title', link='http://www.rte.ie', user=user)
        response = self.client.post(f'/delete/{link.id}/')
        existing_items = Url_Links.objects.filter(id=link.id)
        self.assertEqual(len(existing_items),0)

#Test Toggle Link
    def test_toggle_link(self):
        user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
        self.client.login(username='foo', password='bar')
        link = Url_Links.objects.create(title='Test Title', link='http://www.rte.ie', user=user)
        response = self.client.get(f'/toggle/{link.id}/')
        updated_link = Url_Links.objects.get(id=link.id)  
        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_link.visible, False)

#Test Can Add Link
    def test_can_add_link(self):
        user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
        self.client.login(username='foo', password='bar')
        number_links_before = Url_Links.objects.count()
        response = self.client.post(f'/add/', {'title':'Test New Link', 'link':'http://www.rte.ie'})
        number_links_after = Url_Links.objects.count()
        self.assertEqual(number_links_before+1,number_links_after)