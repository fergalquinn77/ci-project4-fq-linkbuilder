from django.contrib import admin

from .models import url_links
# Register your models here.

@admin.register(url_links)
class url_linksAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    search_fields = ['title']
