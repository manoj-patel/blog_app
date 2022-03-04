from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from user.forms import registration_form,post_form,comment_form
from .models import comments
from django.views.generic import ListView,DetailView
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
    

    posts = post.objects.filter(author=request.user)

    return render(request,'user/home.html',{'posts':posts})


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



#class based view

from .models import post

class postListView(ListView):
    model = post
    template_name = 'user/home.html'
    ordering = ['-date_post']
    context_object_name = 'posts'


from django.http.response import JsonResponse
from django.core import serializers
import json
class postDetailView(DetailView):
    model = post
    template_name = 'user/postdetail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['comments'] = comments.objects.filter(post_super=self.get_object()).order_by('date_comment')
        form = comment_form()
        context['form'] = form
        return context
        
    def post(self,request,*args,**kwargs):
        print(request.POST)
        com = comments.objects.create(post_super=self.get_object(),comment_user=request.user,comment=request.POST['com'])
        cmt = serializers.serialize('json', [ com, ])
        return JsonResponse({'cmt':cmt},safe=False)


@login_required()
def post_post_view(request):
    form = post_form()
    if request.method == 'POST':
        
        form = post_form(request.POST)

        if form.is_valid():
            form.save(request)


    return render(request,'user/blog_post.html',)


@login_required()
def profile_view(request):
    user = request.user
    return render(request,'user/profile.html',{'user':user})


