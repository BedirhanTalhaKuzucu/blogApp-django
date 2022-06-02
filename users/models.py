from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    # image = models.ImageField( upload_to='profilpic/', default= 'profilpic/default.jpg' )
    image = models.CharField(max_length=200, default= 'https://upload.wikimedia.org/wikipedia/commons/1/1e/Default-avatar.jpg')
    bio = models.TextField( max_length= 300, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile( instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        



