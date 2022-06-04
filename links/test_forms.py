from django.test import TestCase
from .forms import LinkForm

class TestLinkForm(TestCase):
    
    def test_image_field_is_not_required(self):
        form = LinkForm({'title': 'Test Title',
        'link':'http://www.rte.ie'
        })
        self.assertTrue(form.is_valid())

    def test_title_is_required(self):
        form = LinkForm({'title': '',
        'link':'http://www.rte.ie'})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
