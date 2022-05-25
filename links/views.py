from django.shortcuts import render, redirect, get_object_or_404, reverse
import requests
from .models import url_links
from accounts.models import profile
from .forms import LinkForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User



@login_required
def links_view(request):
    context = {
        }
    context["dataset"] = url_links.objects.all().filter(user=request.user).order_by('-id')
    return render(request, 'links/index.html', context)

def learn(request):
    if request.user.is_authenticated:
        return links_view(request)
    else:
        return render(request, 'links/learn.html')

@login_required
def add_link(request):
    
    form = LinkForm()

    if request.method == 'POST':
        form = LinkForm(request.POST, request.FILES)
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
            messages.success(request, f'Your link has been added')
            new_form.save()
            return redirect('links-home')
    
    context = {
        'form': form
        }
    return render(request, 'links/add_item.html', context)


@login_required
def edit_link(request, url_links_id):
    link = get_object_or_404(url_links, id=url_links_id)
    
    if request.user == link.user:

        if request.method == 'POST':
            form = LinkForm(request.POST, request.FILES, instance=link)
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
                messages.success(request, f'Your changes have been saved')
                edit_form.save()
                return redirect('links-home')
            
        form = LinkForm(instance=link)
        context = {
            'form': form
            }
        return render(request, 'links/edit_item.html', context)
    else:
        return redirect('links-home')

@login_required
def delete_link(request, url_links_id):
    link = get_object_or_404(url_links, id=url_links_id)
    
    if request.user == link.user:

        if request.method=='POST' and request.user == link.user:
            link.delete()
            return redirect('links-home')
    
        return render(request, 'links/confirm_delete.html',{'link':link})
    else:
        return redirect('links-home')

#The view for displaying links for a particular username visable without login
def links_view_external(request, username):
    user=User.objects.get(username=username)
    user_profile=profile.objects.get(user=user)
    print(user_profile.company_name)
    links=url_links.objects.all().filter(user=user).order_by('-id')
    context = {
        'links':links,
        'user_profile':user_profile
        }
    return render(request, 'links/index_external.html', context)

def toggle_url(request, url_id):
    url = get_object_or_404(url_links, id=url_id)
    url.visible = not url.visible
    url.save()
    return redirect('links-home')

def error_500_view(request,):
    return render(request,'links/500.html')

def error_404_view(request,exception):
    return render(request,'links/404.html')
 