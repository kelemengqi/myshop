from django.contrib import admin
from django.urls import path,include
from django.urls import path,re_path
from app5 import views
from .views import userinfo_msg_form

from .views import upload_file
from .views import userinfo_form


urlpatterns = [
    path('app5/upload_file/', upload_file, name='upload_file'),
    path('app5/userinfoform/', userinfo_form, name='userinfo_form'),
    path('app5/userinfomsgform/', userinfo_msg_form, name='userinfo_msg_form'),
    path('app5/userbaseinfo_modelform/',views.userbaseinfo_modelform),
    path('app5/modelform_user_save/',views.modelform_user_save),
    path('app5/modelform_user_edit/',views.modelform_user_edit),
    path('app5/ajax_login/', views.ajax_login),
    path('app5/ajax_login_data/', views.ajax_login_data),

    

]









