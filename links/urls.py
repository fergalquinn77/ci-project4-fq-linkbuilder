from . import views
from django.urls import path

urlpatterns = [
    path('', views.links_view.as_view(), name='home'),
]

