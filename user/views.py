from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from user.forms import registration_form,post_form
# Create your views here.

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user=user)
            return redirect('home')


        else:
            messages.error(request,"invalid username or password!!!")
            return redirect('login')


    return render(request,'user/login.html')


def home_view(request):
    
    return render(request,'user/base.html')


def register_view(request):
    form = registration_form()
    if request.method == "POST":
        form = registration_form(request.POST)
        if form.is_valid():
            if not form.user_exit():
                form.save()
                
                return redirect('login')
            else:
                messages.set_level(request,messages.DEBUG)
                messages.error(request,"username already exists!!!!")

                return redirect('register')

    return render(request,'user/signup.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')



def post_get_view(request):
    pass

@login_required()
def post_post_view(request):
    form = post_form()
    if request.method == 'POST':
        print(request.user)
        form = post_form(request.POST)
        if form.is_valid():
            form.save()


    return render(request,'user/blog_post.html',)



