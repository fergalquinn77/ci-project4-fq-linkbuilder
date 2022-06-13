from django.contrib import admin
from django.contrib.auth.models import User
from .models import Url_Links


@admin.register(Url_Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    search_fields = ['user__username', 'title']
    list_filter = ('user',)

