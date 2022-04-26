from django.shortcuts import render
from django.views import generic, View
from .models import Post

# Create your views here.

class links_view(generic.ListView):
    model = url_links
    template_name = "index.html"
