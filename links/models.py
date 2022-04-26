from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class url_links(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    link = models.URLField(blank=False)
    url_image = CloudinaryField('image', default='url_placeholder')
    visible = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class profile(User):
    company_name = models.CharField(max_length=50,blank=True)
    facebook = models.CharField(max_length=50,blank=True)
    instagram = models.CharField(max_length=50,blank=True)
    twitter = models.CharField(max_length=50,blank=True)
    profile_image = CloudinaryField('image', default='profile_placeholder')
    

    def __str__(self):
        return f"Profile for {self.username}"
