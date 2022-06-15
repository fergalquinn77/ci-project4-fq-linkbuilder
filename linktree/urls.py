from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from links import views as links_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', links_views.learn, name='home'),
    path('index/', links_views.links_view, name='links-home'),
    # Account related
    path('register/', accounts_views.register, name='register'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', accounts_views.profile, name='profile'),
    # URL Link Model related
    path('add/', links_views.add_link, name='add-link'),
    path('edit/<int:url_links_id>/', links_views.edit_link, name='edit-link'),
    path('toggle/<url_id>/', links_views.toggle_url, name='toggle'),
    path('delete/<int:url_links_id>/', links_views.delete_link,
         name='delete-link'),
    path('counter/<int:linkid>/', links_views.link_count_then_redirect,
         name='click-counter'),
    # Support model related
    path('support/', accounts_views.display_tickets,
         name='open-support-tickets'),
    path('add-ticket/', accounts_views.add_support_ticket,
         name='add-support-ticket'),
    path('toggle-ticket-status/<ticket_id>/',
         accounts_views.toggle_ticket_status, name='toggle-ticket-status'),
    path('ticket-details/<ticket_id>/', accounts_views.ticket_details,
         name='ticket-details'),
    # External view - no login required
    path('user/<username>/', links_views.links_view_external,
         name='external-view'),
    # Password resetting related
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'links.views.error_404_view'
handler500 = 'links.views.error_500_view'
