from django.contrib import admin
from .models import Profile
# Register your models here.


@admin.register(Profile)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name')
    search_fields = ['user__username', 'company_name']
