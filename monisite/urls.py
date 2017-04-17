#coding:utf-8
from django.conf.urls import url
from django.contrib import admin

import xadmin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
