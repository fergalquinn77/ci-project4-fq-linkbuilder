from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import url_links
from .forms import LinkForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# def home(request):
#     context = {
#         'urls':url_links.objects.all()
#     }
#     return render(request,'index.html', context)

# def about(request):
#     return HttpResponse(('<h1>About</h1>'))

class links_view(generic.ListView):
    model = url_links
    template_name = "index.html"

# class add_item(generic.ListView):
#     model = url_links
#     template_name = "add_item.html"

# class LinkCreateView(LoginRequiredMixin, CreateView):
#     model = url_links
#     fields = ['title', 'link', 'url_image']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)