from django.urls import path
from . import views
from .views import Item

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('video',views.video,name='video'),
    path('homeComment',views.homeComment,name='homeComment'),
    path('signup',views.handleSignup, name='handleSignup'),
    path('login',views.handleLogin, name='handleLogin'),
    path('logout',views.handleLogout, name='handleLogout'),
    path('<str:slug>',views.homeviews,name='homeviews')
]