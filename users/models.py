from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    """Extended the built in user model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ae_id = models.CharField(max_length=20, default="", blank="", help_text="This is used to link AE accounts to your account") #todo set editable=False for production
    ae_token = models.TextField(default="", blank=True, editable=False)

    def __str__(self):
        """displays fstring when user is returned"""
        return f'{self.user.username} Profile'


# TODO Clean this up
@receiver(post_save, sender=User)  # Auto creates a profile for each new user
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)  # Auto creates a profile for each new user
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
