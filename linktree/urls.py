from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('links.urls'), name='link-urls'),
    path('register/', accounts_views.register, name='register'),
    path('accounts/', include('allauth.urls')),
    path('profile/', accounts_views.profile, name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('links.urls'), name='link-urls'),
#     path('accounts/', include('allauth.urls')),
# ]