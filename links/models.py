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

    def __str__(self):
        return self.title

class Url_Clicks(models.Model):
    count = models.PositiveIntegerField(default=0)
    link = models.ForeignKey(Url_Links, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.link} clicked {self.count}"
