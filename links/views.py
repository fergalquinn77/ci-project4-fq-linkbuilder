from django.shortcuts import render, redirect, get_object_or_404, reverse
import requests
from .models import Url_Links, Support_Messages, Support_Ticket
from accounts.models import Profile
from .forms import LinkForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.base import RedirectView


# View for displaying user links (login required)
@login_required
def links_view(request):
    data = Url_Links.objects.all().filter(user=request.user)
    context = {
        }
    context["dataset"] = data.order_by('-id')
    return render(request, 'links/index.html', context)


# View for root directory/homepage (no login required)
def learn(request):
    if request.user.is_authenticated:
        return links_view(request)
    else:
        return render(request, 'links/learn.html')


# View for adding links (login required)
@login_required
def add_link(request):
    form = LinkForm()
    if request.method == 'POST':
        form = LinkForm(request.POST, request.FILES)
        form_url = request.POST.get('link')
        url_pass = ''
        try:
            requests.get(form_url)
            url_pass = True
        except requests.exceptions.ConnectionError:
            messages.warning(request, 'Invalid URL entered')
            url_pass = False
        if form.is_valid() and url_pass is True:
            new_form = form.save(commit=False)
            new_form.user = request.user
            messages.success(request, f'Your link has been added')
            new_form.save()
            return redirect('links-home')
    context = {
        'form': form
        }
    return render(request, 'links/add_item.html', context)


# View for editing links (login required)
@login_required
def edit_link(request, url_links_id):
    link = get_object_or_404(Url_Links, id=url_links_id)
    if request.user == link.user:
        if request.method == 'POST':
            form = LinkForm(request.POST, request.FILES, instance=link)
            form_url = request.POST.get('link')
            url_pass = ''
            try:
                requests.get(form_url)
                url_pass = True
            except requests.exceptions.ConnectionError:
                messages.warning(request, 'Invalid URL entered')
                url_pass = False
            if form.is_valid() and url_pass is True:
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
        messages.warning(request, 'You do not have access to this page')
        return redirect('links-home')


# View for deleting links (login required)
@login_required
def delete_link(request, url_links_id):
    link = get_object_or_404(Url_Links, id=url_links_id)
    if request.user == link.user:
        if request.method == 'POST' and request.user == link.user:
            link.delete()
            return redirect('links-home')
        return render(request, 'links/confirm_delete.html', {'link': link})
    else:
        messages.warning(request, 'You do not have access to this page')
        return redirect('links-home')


# The view for displaying links for a particular username visable without login
def links_view_external(request, username):
    user_display = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_display)
    links = Url_Links.objects.all().filter(user=user_display).order_by('-id')
    context = {
        'links': links,
        'user_profile': user_profile
        }
    return render(request, 'links/index_external.html', context)

# Render page from link click on external landing page
def link_count_then_redirect(request, linkid):
    link = url = get_object_or_404(Url_Links, id=linkid)
    link.click_count += 1
    link.save()
    return redirect(link.link)

# Used for toggling links from visible to not visible
@login_required()
def toggle_url(request, url_id):
    url = get_object_or_404(Url_Links, id=url_id)
    if request.user == url.user:
        url.visible = not url.visible
        url.save()
        return redirect('links-home')
    else:
        messages.warning(request, 'You do not have access to this page')
        return redirect('links-home')

# Used to display all support queries
@login_required()
def display_tickets(request):
    tickets = Support_Ticket.objects.all()
    context = {
        'tickets': tickets
        }
    return render(request, 'links/support.html', context)


# 500 and 404 error pages
def error_500_view(request,):
    return render(request, 'links/500.html')


def error_404_view(request, exception):
    return render(request, 'links/404.html')
