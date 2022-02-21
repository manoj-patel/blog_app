from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

gender_choices = (
    (0,'male'),
    (1,'female'),
    (2,"not specified"),
)


class post(models.Model):
    title = models.CharField(max_length=1111)
    content = models.TextField()
    date_post = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - "+self.author.username


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img = models.ImageField(default='download.png',upload_to='profile')
    dob = models.DateField(default="1996-01-01")
    gender = models.IntegerField(choices=gender_choices)

    def __str__(self):
        return self.user.username + " Profile"


    def save(self, *args, **kwargs):
	    super(profile,self).save(*args, **kwargs)





