from django.contrib import admin
from django.contrib.auth.models import User
from .models import url_links


@admin.register(url_links)
class url_linksAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    search_fields = ['user__username', 'title']
    list_filter = ('user',)
