from . import views
from django.urls import path
from django.urls import path, include
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.links_view.as_view(), name='links-home'),
    path('add/', views.add_link, name='add-link')
]

# urlpatterns = [
#     path('', views.links_view.as_view(), name='home'),
#     path('links/new/', LinkCreateView.as_view(), name='link-create'),
# ]

