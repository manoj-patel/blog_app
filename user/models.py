from distutils.command.upload import upload
from email.policy import default
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
    like_count = models.IntegerField(default=0)
    image = models.ImageField(default="post.jpg",upload_to='posts')
    def __str__(self):
        return self.title + " - "+self.author.username


    def get_date(self):
        return self.date_post.date()


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img = models.ImageField(default='download.png',upload_to='profile')
    dob = models.DateField(default="1996-01-01")
    gender = models.IntegerField(choices=gender_choices)
    
    def __str__(self):
        return self.user.username + " Profile"


    def save(self, *args, **kwargs):
	    super(profile,self).save(*args, **kwargs)


class comments(models.Model):
    date_comment = models.DateTimeField(default=timezone.now)
    date_update_comment = models.DateTimeField(default=timezone.now)
    post_super = models.ForeignKey(post,on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.post_super.title +" - "+ self.comment_user.first_name

    def get_date(self):
        return self.date_comment.date()
 