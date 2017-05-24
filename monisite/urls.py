#coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import View
from django.views.generic.base import TemplateView

import xadmin

from orm.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #
    url(r'^ormlogin/$',TemplateView.as_view(template_name='ormlogin.html'),name='ormlogin'),
    url(r'^ormindex/$',TemplateView.as_view(template_name='ormindex.html'),name='ormindex'),
    # url(r'^ormmoni/$', TemplateView.as_view(template_name='ormmoni.html'), name='ormmoni'),
    url(r'ormmoni/$',ormmoni),
    url(r'display_target_info/$',display_target_info)

]
