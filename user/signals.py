from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import profile
from django.contrib.auth.models import User


@receiver(post_save,sender=User)

def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance,gender=0)


@receiver(post_save,sender=User)

def save_Profile(sender,instance,**kwargs):
    instance.profile.save()





    


