#coding:utf-8
from django.contrib import admin
from orm.models import *
# Register your models here.


class RepQueueAdmin(admin.ModelAdmin):
    list_display = ['describe','src_ip','src_path','tgt_ip','tgt_path', 'add_user','add_time']
    # list_editable = ['describe','src_ip','src_path','tgt_ip','tgt_path', 'add_time']
    def save_model(self, request, obj, form, change):
        print request.user
        if getattr(obj,'add_user',None):
            obj.add_user=request.user
            print 'obj.add_user:',obj.add_user
            obj.save()


admin.site.register(rep_queue,RepQueueAdmin)