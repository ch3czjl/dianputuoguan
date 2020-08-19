#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: urls.py
@time: 2016/11/2 下午7:15
"""
from django.conf.urls import url
from django.urls import path
from . import views
from .views import bangdingview
from django.utils.decorators import method_decorator



app_name = "dianptg"

urlpatterns = [
    path('',views.post_list),
    url(r'^bangding/$',views.bangdingview.as_view(success_url="/"),name='bangding'),
    url(r'^adddianpudatebase/$',views.adddianpudatebase),
    url(r'^bangdinghou/$',views.bangdinghou),
    ]
