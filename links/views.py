from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import url_links
from .forms import LinkForm
from django.contrib.auth.decorators import login_required
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

class links_detail_view(generic.DetailView):
    model = url_links
    template_name = "index.html"

@login_required
def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('links-home')
    form = LinkForm()
    context = {
        'form': form
        }
    return render(request, 'add_item.html', context)

# class add_item(generic.ListView):
#     model = url_links
#     template_name = "add_item.html"

# class LinkCreateView(LoginRequiredMixin, CreateView):
#     model = url_links
#     fields = ['title', 'link', 'url_image']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)