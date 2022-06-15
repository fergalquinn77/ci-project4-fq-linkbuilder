from django.contrib import admin
from .models import Profile, Support_Tickets, Tickets_Messages
# Register your models here.


@admin.register(Profile)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name')
    search_fields = ['user__username', 'company_name']

@admin.register(Support_Tickets)
class SupportAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    search_fields = ['user__username', 'title']
    list_filter = ('user','status')

@admin.register(Tickets_Messages)
class SupportAdmin(admin.ModelAdmin):
    list_display = ['user', 'ticket','message']
    search_fields = ['user__username', 'ticket']
    list_filter = ('user',)

