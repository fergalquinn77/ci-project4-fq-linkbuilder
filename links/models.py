from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Model for user links
class Url_Links(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    link = models.URLField(blank=False)
    url_image = CloudinaryField('image', default='url_placeholder')
    visible = models.BooleanField(default=True)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

STATUS = ((0, "New"), (1, "Open"), (2, "Closed"))

# Model for dealing with support tickets
class Support_Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=False)
    query = models.TextField(blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

class Support_Messages(models.Model):
    ticket = models.ForeignKey(Support_Ticket, on_delete=models.CASCADE,
                             related_name="Ticket")
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.user}"


