from django.shortcuts import render

# Create your views here.
# app4/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # 假设你有一个名为 index.html 的模板文件
