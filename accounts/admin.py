from django.contrib import admin
from .models import Profile, Support_Tickets, Tickets_Messages


# Profile Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name')
    search_fields = ['user__username', 'company_name']


# Support query admin
@admin.register(Support_Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    search_fields = ['user__username', 'title']
    list_filter = ('user', 'status')


# Support Tickets Admin
@admin.register(Tickets_Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['user', 'ticket', 'message']
    search_fields = ['user__username', 'ticket']
    list_filter = ('user',)
