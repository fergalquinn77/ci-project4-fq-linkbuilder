from django.contrib import admin
from .models import profile
# Register your models here.


@admin.register(profile)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name')
    search_fields = ['user__username', 'company_name']
