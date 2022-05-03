from . import views
from django.urls import path

from django.urls import path, include

urlpatterns = [
    path('', views.links_view.as_view(), name='links-home'),
    # path('about/', views.about, name='links-about')
]

# urlpatterns = [
#     path('', views.links_view.as_view(), name='home'),
#     path('links/new/', LinkCreateView.as_view(), name='link-create'),
# ]

