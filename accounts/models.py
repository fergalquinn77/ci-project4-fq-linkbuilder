from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save


# Model for user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, blank=True)
    facebook = models.URLField(max_length=50, blank=True)
    instagram = models.URLField(max_length=50, blank=True)
    twitter = models.URLField(max_length=50, blank=True)
    profile_image = CloudinaryField('Screenshot', default='profile_placeholder')

    def __str__(self):
        return f"Profile for {self.user}"

STATUS = ((0, "Open"), (1, "Closed"))

# Model for dealing with support tickets
class Support_Tickets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="SupportTickets")
    title = models.CharField(max_length=200,blank=False)
    query = models.TextField(blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    query_image = CloudinaryField('image', default='url_placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    class Meta:
        verbose_name_plural = 'Supprt Tickets'

    def __str__(self):
        return self.title

# Model for dealing with messages relating to support tickets
class Tickets_Messages(models.Model):
    ticket = models.ForeignKey(Support_Tickets, on_delete=models.CASCADE,
                             related_name="Tickets")
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.message} by {self.user}"

    class Meta:
        verbose_name_plural = 'Support Responses'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.profile.save()