from django import forms
from django.forms import ModelForm, fields
from . models import Url_Links


# Form for CRUD of Links
class LinkForm(forms.ModelForm):
    class Meta:
        model = Url_Links
        fields = ['title', 'link', 'url_image']
