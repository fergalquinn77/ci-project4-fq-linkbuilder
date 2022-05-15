from . import views
from django.urls import path
from django.urls import path, include
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.links_view, name='links-home'),
    path('add/', views.add_link, name='add-link'),
    path('edit/<int:url_links_id>/', views.edit_link, name='edit-link'),
    path('delete/<int:url_links_id>/', views.delete_link, name='delete-link'),   
]

handler404 = 'links.views.error_404_view'
handler500 = 'links.views.error_500_view'

