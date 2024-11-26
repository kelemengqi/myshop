
from django.contrib import admin
from django.urls import path,include
from django.urls import path,re_path
from app3 import views
urlpatterns = [
    path('var/',views.var),
    path('for_label/',views.for_label),
    path('filter/',views.filter)
    
]

