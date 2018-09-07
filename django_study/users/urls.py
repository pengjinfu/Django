#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.9.1
from django.conf.urls import url

from users import views
# urlpatterns是被django自动识别的路由列表变量
urlpatterns =[
    # 每个路由信息都需要使用url函数来构造
    # url(路径, 视图)
    url(r'index/$',views.index)
]