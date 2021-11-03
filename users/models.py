from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    """Extended the built in user model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ae_token = models.TextField(default="", blank=True)
    image = models.ImageField(default='default.JPG', upload_to='profile_pics')

    def __str__(self):
        """displays fstring when user is returned"""
        return f'{self.user.username} Profile'

