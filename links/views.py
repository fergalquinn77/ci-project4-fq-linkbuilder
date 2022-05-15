from django.shortcuts import render, redirect, get_object_or_404, reverse
import requests
from .models import url_links
from accounts.models import profile
from .forms import LinkForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def links_view(request):
    context = {
        }
    context["dataset"] = url_links.objects.all().filter(user=request.user)
    return render(request, 'index.html', context)

@login_required
def add_link(request):
    
    form = LinkForm()

    if request.method == 'POST':
        form = LinkForm(request.POST)
        form_url = request.POST.get('link')
        url_pass=''
        try:
            requests.get(form_url)
            url_pass=True
        except requests.exceptions.ConnectionError:
            messages.warning(request, 'Invalid URL entered')
            url_pass=False
        if form.is_valid() and url_pass==True:
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('links-home')
    
    context = {
        'form': form
        }
    return render(request, 'add_item.html', context)


@login_required
def edit_link(request, url_links_id):
    link = get_object_or_404(url_links, id=url_links_id)
    
    if request.user == link.user:

        if request.method == 'POST':
            form = LinkForm(request.POST, instance=link)
            form_url = request.POST.get('link')
            url_pass=''
            try:
                requests.get(form_url)
                url_pass=True
            except requests.exceptions.ConnectionError:
                messages.warning(request, 'Invalid URL entered')
                url_pass=False
            if form.is_valid() and url_pass==True:
                edit_form = form.save(commit=False)
                edit_form.user = request.user
                edit_form.save()
                return redirect('links-home')
            
        form = LinkForm(instance=link)
        context = {
            'form': form
            }
        return render(request, 'edit_item.html', context)
    else:
        return redirect('links-home')

@login_required
def delete_link(request, url_links_id):
    link = get_object_or_404(url_links, id=url_links_id)
    
    if request.user == link.user:

        if request.method=='POST' and request.user == link.user:
            link.delete()
            return redirect('links-home')
    
        return render(request, 'confirm_delete.html',{'link':link})
    else:
        return redirect('links-home')


