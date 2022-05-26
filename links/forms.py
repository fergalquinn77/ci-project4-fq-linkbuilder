from django import forms
from django.forms import ModelForm, fields
from . models import url_links

# Form for CRUD of Links
class LinkForm(forms.ModelForm):
    class Meta:
        model = url_links
        fields = ['title', 'link', 'url_image']
