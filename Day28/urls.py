from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.homepage, name='homePage'),
    path('home/', views.homepage, name='homePage'),
    path('about/', views.aboutpage, name='aboutPage'),
    path('loginform/', views.loginform, name='loginForm'),
    path('logincheck/', views.logincheck, name='loginCheck'),
    
]