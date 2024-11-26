from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# app5/views.py

from app4.models import UserBaseInfo  # 更改为正确的相对路径

from .forms import UserBaseInfoModelForm, UserInfoForm
import os
from .forms import UserInfo_Msg_Form

def upload_file(request):
    if request.method == "GET":
        return render(request, "5/upload.html")
    
    # 请求方法为POST时，进行处理
    if request.method == "POST":
        # 获取上传的文件
        myFile = request.FILES.get("myfile", None)
        
        if myFile:
            # 二进制的写操
            path = 'media/uploads/'
            
            if not os.path.exists(path):
                os.makedirs(path)
            
            dest = open(os.path.join(path, myFile.name), 'wb+')
            for chunk in myFile.chunks():
                # 分块写入文件
                dest.write(chunk)
            dest.close()
            return HttpResponse("上传完成!")
        else:
            return HttpResponse("没有上传文件!")


def userinfo_form(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            # 处理有效数据
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            return HttpResponse(f'提交成功: {username}, {email}, {age}岁')
    else:
        form = UserInfoForm()
    
    return render(request, '5/userinfo.html', {'form': form})

# Create your views here.


def userinfo_msg_form(request):
    if request.method == "GET":
        myform = UserInfo_Msg_Form()
        return render(request, "5/userinfoform.html", {'form_obj': myform})
    else:
        f = UserInfo_Msg_Form(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            print(f.cleaned_data["username"])
            print(f.data)
            return HttpResponse("表单提交成功!")  # 或者根据需要进行其他处理
        else:
            errors = f.errors
            print(errors)
            return render(request, "5/userinfoform.html", {'form_obj': f, 'errors': errors})
    
    return render(request, "5/userinfoform.html", {'form_obj': f})

def userbaseinfo_modelform(request):
    if request.method == "GET":
        myform = UserBaseInfoModelForm()
        return render(request, "5/userbaseinfoform.html", {'form_obj': myform})
    else:
        f = UserBaseInfoModelForm(request.POST)
        if f.is_valid():
            print(f.cleaned_data)  # 修正了这里的拼写
            print(f.cleaned_data["username"])
            print(f.data)
        else:
            errors = f.errors
            print(errors)
            return render(request, "5/userbaseinfoform.html", {'form_obj': f, 'errors': errors})

    return render(request, "5/userbaseinfoform.html", {'form_obj': f})

def modelform_user_save(request):
    if request.method == "GET":
        myform = UserBaseInfoModelForm()
        return render(request, "5/userbaseinfoform.html", {'form_obj': myform})
    else:
        f = UserBaseInfoModelForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('success_url')  # 替换为成功后的跳转URL
        else:
            errors = f.errors
            print(errors)
            return render(request, "5/userbaseinfoform.html", {'form_obj': f, 'errors': errors})

    return render(request, "5/userbaseinfoform.html", {'form_obj': f})

def modelform_user_edit(request, id):
    if request.method == "GET":
        try:
            user = UserBaseInfo.objects.get(id=id)
            if user:
                myform = UserBaseInfoModelForm(instance=user)
                return render(request, "5/userbaseinfoform.html", {'form_obj': myform})
        except UserBaseInfo.DoesNotExist:
            return render(request, "5/userbaseinfoform.html", {'form_obj': UserBaseInfoModelForm()})

    else:
        user = UserBaseInfo.objects.get(id=id)
        f = UserBaseInfoModelForm(request.POST, instance=user)
        if f.is_valid():
            f.save()
            return redirect('success_url')  # 替换为成功后的跳转URL
        else:
            errors = f.errors
            print(errors)
            return render(request, "5/userbaseinfoform.html", {'form_obj': f, 'errors': errors})

    return render(request, "5/userbaseinfoform.html", {'form_obj': f})

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render

# CSRF exempt for ajax login
@csrf_exempt
def ajax_login(request):
    return render(request, "5/ajax_login.html")

# CSRF exempt for handling login data
@csrf_exempt
def ajax_login_data(request):
    print(request.POST)
    # 获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    # 判断并返回 json 数据
    if username == "admin" and password == "123456":
        return JsonResponse({"code": 1, "msg": "登录成功"})
    else:
        return JsonResponse({"code": 0, "msg": "登录失败"})
