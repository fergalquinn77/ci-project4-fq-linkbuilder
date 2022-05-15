from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from links import views as links_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('links.urls'), name='link-urls'),
    path('register/', accounts_views.register, name='register'),
    path('accounts/', include('allauth.urls')),
    # path('profile_update/', accounts_views.profile_update, name='profile-update'),
    path('profile/', accounts_views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'links.views.error_404_view'
handler500 = 'links.views.error_500_view'