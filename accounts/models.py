from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50,blank=True)
    facebook = models.CharField(max_length=50,blank=True)
    instagram = models.CharField(max_length=50,blank=True)
    twitter = models.CharField(max_length=50,blank=True)
    profile_image = CloudinaryField('image', default='profile_placeholder')
    
    def __str__(self):
        return f"Profile for {self.username}"

# Create your models here.