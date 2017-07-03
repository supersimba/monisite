#coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import View
from django.views.generic.base import TemplateView

from orm.views import *
# import xadmin

from orm.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #
    url(r'^ormlogin/$',TemplateView.as_view(template_name='ormlogin.html'),name='ormlogin'),
    # url(r'^ormindex/$',TemplateView.as_view(template_name='ormindex.html'),name='ormindex'),
    url(r'^ormlogin_action/$',ormlogin_action,name='ormlogin_action'),
    url(r'^ormlogout/$',ormlogout,name='ormlogout'),
    url(r'^ormindex/$',ormindex,name='ormindex'),
    # url(r'^ormmoni/$', TemplateView.as_view(template_name='ormmoni.html'), name='ormmoni'),
    url(r'ormmoni/$',ormmoni,name='ormmoni'),
    url(r'^display_target_info/$',display_target_info),
    url(r'^display_source_info/$',display_source_info),
    url(r'^ormlogs/$',display_replogs,name='ormlogs'),
    url(r'^ormlogs/(?P<RID>\d+)/(?P<TYPE>\d+)$',display_replogs,name='ormlogs'),
    #执行 CHECK脚本函数
    url(r'^check_process/$',check_process),
    #显示 日志
    url(r'^display_log/$',display_log),
    #同步操作
    url(r'^ormoper/(?P<RID>\d+)$',ormoper,name='ormoper'),
    #
    url(r'^sync_oper/$',sync_oper),
    #
    url(r'^edit_mapping',edit_mapping),
]
