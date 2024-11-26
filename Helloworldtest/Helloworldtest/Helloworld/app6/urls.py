from django.contrib import admin
from django.urls import path,include
from django.urls import path,re_path
from app6  import views

urlpatterns = [
    path('app6/user_reg/', views.user_reg),
    path('app6/user_login/', views.user_reg),]
