from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from links import views as links_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', links_views.learn, name='home'),
    path('index/', links_views.links_view, name='links-home'),
    path('register/', accounts_views.register, name='register'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', accounts_views.profile, name='profile'),
    path('add/', links_views.add_link, name='add-link'),
    path('edit/<int:url_links_id>/', links_views.edit_link, name='edit-link'),
    path('delete/<int:url_links_id>/', links_views.delete_link, name='delete-link'),
    path('<username>/', links_views.links_view_external, name='external-view'),
    path('toggle/<url_id>', links_views.toggle_url, name='toggle'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'links.views.error_404_view'
handler500 = 'links.views.error_500_view'
