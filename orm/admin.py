#coding:utf-8
from django.contrib import admin
from orm.models import *
# Register your models here.


class RepQueueAdmin(admin.ModelAdmin):
    list_display = ['describe','src_ip','src_path','tgt_ip','tgt_path', 'add_user','add_time']


admin.site.register(rep_queue,RepQueueAdmin)