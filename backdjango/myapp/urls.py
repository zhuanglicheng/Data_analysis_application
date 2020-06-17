# -*- coding:utf-8 -*-
# 作者：庄立成
# 日期：2020/6/17 10:23
# 工具：PyCharm
# 文件 :urls.py
# Python版本：3.5.2
from django.conf.urls import url
from .views import index,method_get
urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^method_get/$', method_get, name='method_get'),
]