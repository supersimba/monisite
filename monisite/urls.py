#coding:utf-8
from django.conf.urls import url
# from django.contrib import admin

import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
]
