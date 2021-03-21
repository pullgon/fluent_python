# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/3/17 1:28
# Description: booktest app route

# from django.conf.urls import include
from django.urls import path
from .views import my_render

urlpatterns = [path("index/", my_render)]
