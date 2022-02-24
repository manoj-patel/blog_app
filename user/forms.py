from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import post

class registration_form(UserCreationForm):
    fname = forms.CharField(max_length=200)
    lname = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(max_length=200)
    password2 = forms.CharField(max_length=200)


    class Meta:
        model = User
        fields = ['fname','lname','email','password1','password2']


    def user_exit(self):
        username = self.cleaned_data['email']
        if User.objects.filter(username=username).exists():
            return True

        return False


    def save(self):
        fname = self.cleaned_data['fname']
        lname = self.cleaned_data['lname']
        email=username = self.cleaned_data['email']
        password = self.cleaned_data['password1']

        user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)




class post_form(ModelForm):
    title = forms.CharField(max_length=200)
    content = forms.CharField(max_length=10000)

    class Meta:
        model = post
        fields = ['title','content']


    
