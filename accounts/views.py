from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Support_Tickets, Tickets_Messages
from .forms import *


# User Registration
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})


# Profile Creation
@login_required
def profile(request):
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST,
                               request.FILES,
                               instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)


# Used to display all support queries
@login_required()
def display_tickets(request):
    tickets = Support_Tickets.objects.all().order_by("-created_on")
    tickets_open = tickets.filter(status="0", user=request.user)
    ticket_messages = Tickets_Messages.objects.filter(ticket=tickets)
    context = {
        'tickets_open': tickets_open,
        'ticket_messages': ticket_messages
        }
    return render(request, 'accounts/support.html', context)


# Add support ticket
@login_required
def add_support_ticket(request):
    form = SupportTicketForm()
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            messages.success(request, f'Your query has been added')
            new_form.save()
            return redirect('open-support-tickets')
    context = {
        'form': form
        }
    return render(request, 'accounts/add_ticket.html', context)


# Used for toggling links from visible to not visible
@login_required()
def toggle_ticket_status(request, ticket_id):
    ticket = get_object_or_404(Support_Tickets, id=ticket_id)
    if request.user == ticket.user:
        if ticket.status == 0:
            ticket.status = 1
            ticket.save()
        else:
            ticket.status = 0
            ticket.save

        return redirect('open-support-tickets')
    else:
        messages.warning(request, 'You do not have access to this page')
        return redirect('links-home')


# Used for getting support ticket details
@login_required()
def ticket_details(request, ticket_id):

    ticket = get_object_or_404(Support_Tickets, id=ticket_id)

    form = SupportMessageForm()
    if request.method == 'POST':
        form = SupportMessageForm(request.POST)
        if request.user == ticket.user:
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.ticket = Support_Tickets.objects.get(id=ticket_id)
                messages.success(request, f'Your message has been posted')
                new_form.save()
                return redirect('ticket-details', ticket.id)
        else:
            messages.warning(request, 'You do not have access to this page')
            return redirect('links-home') 

    if request.user == ticket.user:
        ticket_messages = Tickets_Messages.objects.all().filter(ticket=ticket)
        context = {
            'ticket': ticket,
            'ticket_messages': ticket_messages,
            'form': form
            }
        return render(request, 'accounts/ticket_detail.html', context)
    else:
        messages.warning(request, 'You do not have access to this page')
        return redirect('links-home')
