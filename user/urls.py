from django.contrib import admin
from django.urls import path
from . import views
from .views import postDetailView, postListView

urlpatterns = [
    path('', postListView.as_view(),name="home"),
    path('login/',views.login_view,name="login"),
    path('register/',views.register_view,name="register"),
    path('logout/',views.logout_view,name="logout"),
    path('createpost/',views.post_post_view,name="createpost"),
    path('profile/',views.profile_view,name="profile"),
    path('post/<int:pk>',postDetailView.as_view(),name="viewpost"),
    path('post/comment',postDetailView.as_view(),name="comment"),
]
