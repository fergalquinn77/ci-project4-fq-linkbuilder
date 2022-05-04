from django.shortcuts import render, redirect, get_object_or_404, reverse
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

class links_view(LoginRequiredMixin, generic.ListView):
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

@login_required
def edit_link(request, url_links_id):
    item = get_object_or_404(url_links, id=url_links_id)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=item)
        if form.is_valid():
            edit_form = form.save(commit=False)
            edit_form.user = request.user
            edit_form.save()
            return redirect('links-home')
        
    form = LinkForm(instance=item)
    context = {
        'form': form
        }
    return render(request, 'edit_item.html', context)

@login_required
def delete_link(request, url_links_id):
    item = get_object_or_404(url_links, id=url_links_id)
    item.delete()
    return redirect('links-home')