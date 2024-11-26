from django.contrib import admin
from django.urls import path,include
from django.urls import path,re_path
from app2 import views
urlpatterns = [
    path('app2/index',views.index,name='app2_index'),
    path('app2/show_param_int/<int:id>',views.show_param_int),
    path('app2/article/<uuid:id>/',views.show_uuid,name='show_uuid'),
    path('app2/article/<slug:q>/',views.show_slug,name='show_slug'),
    re_path(r'app2/list/(?P<year>\d{4})/',views.article_list),
    re_path(r'app2/page/(?P<page>\d+)&key=(?P<key>\w+)',views.article_page,name="article_page"),
    path('app2/url_reverse/',views.url_reverse,name='app2_rul_reverse'),



]
