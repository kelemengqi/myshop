# app4/urls.py

from django.urls import path
from . import views  # 导入视图

urlpatterns = [
    path('index/', views.index, name='index'),  # 假设你有一个名为 index 的视图函数
]
