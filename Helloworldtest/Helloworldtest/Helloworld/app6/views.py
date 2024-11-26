from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def user_reg(request):
    if request.method == "GET":
        return render(request, "6/user_reg.html")

    if request.method == "POST":
        uname = request.POST.get("username", "")
        pwd = request.POST.get("password", "")
        
        if User.objects.filter(username=uname).exists():
            info = "用户已经存在"
        else:
            d = dict(username=uname, password=pwd, email='1110111.com', is_staff=1, is_active=1, is_superuser=1)
            user = User.objects.create_user(**d)
            info = "注册成功,请登录"
        
        return render(request, '6/user_reg.html', {"info": info})


def user_login(request):
    if request.method == "GET":
        return render(request, "6/user_login.html")
    
    if request.method == "POST":
        uname = request.POST.get("username", "")
        pwd = request.POST.get("password", "")
        
        if User.objects.filter(username=uname):  # 判断用户是否存在
            # 如果存在，进行验证
            user = authenticate(username=uname, password=pwd) # type: ignore
            
            if user:  # 如果验证通过
                if user.is_active:  # 如果用户状态为激活
                    login(request, user)  # type: ignore # 进行登录操作，完成 session 的设置
                    info = "登录成功"
                else:
                    info = "用户还未激活"
            else:
                info = "账号密码不对，请重新输入"
        else:
            info = "用户账号不存在，请查询"
        
        return render(request, '6/user_login.html', {"info": info})
