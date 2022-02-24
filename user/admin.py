from django.contrib import admin
from .models import post,profile,comments
# Register your models here.

admin.site.register([post,profile,comments])
