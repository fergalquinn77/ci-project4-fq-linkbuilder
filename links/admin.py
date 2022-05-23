from django.contrib import admin
from django.contrib.auth.models import User
from .models import url_links
# Register your models here.

@admin.register(url_links)
class url_linksAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    search_fields = ['user','title']
