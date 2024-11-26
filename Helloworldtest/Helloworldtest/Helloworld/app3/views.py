from django.shortcuts import render
import datetime
def var(request):
    lists=['Java','Python','C','JavaScript']
    dicts={'姓名':'张三','年龄':25,'性别':'男'}
    return render(request,'3/var.html',{'lists':lists,'dicts':dicts})

def for_label(request):
    dict1={'书名':'Django开发','价格':80,'作者':'张三'}
    dict2={'书名':'Python开发','价格':90,'作者':'张三'}
    dict3={'书名':'Java开发','价格':100,'作者':'张三'}
    lists=[dict1,dict2,dict3]
    return render(request,'3/for_label.html',{'lists':lists})

def filter(request):
    str1="abcdefg"
    str2="ABCDEFG"
    slice_str="1234567890"
    time_str=datetime.datetime.now()
    return render(request,'3/filter.html',{"str1":str1,"str2":str2,"slice_str":slice_str,"time_str":time_str})

    
# Create your views here.
