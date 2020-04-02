from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pub(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    drinks = models.IntegerField(default=0)
    atmosphere = models.IntegerField(default=0)
    service = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='pub_images', blank=True)
    
    def __str__(self): 
        return self.name
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    crawl = models.ManyToManyField(Pub)
    def __str__(self):
        return self.user.username
