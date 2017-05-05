#coding:utf-8
from django.contrib import admin
from orm.models import *
# Register your models here.


class RepQueueAdmin(admin.ModelAdmin):
    list_display = ['describe','src_ip','src_path','tgt_ip','tgt_path', 'add_user','src_script_path','tgt_script_path','add_time']
    # list_editable = ['describe','src_ip','src_path','tgt_ip','tgt_path', 'add_time']
    def save_model(self, request, obj, form, change):
        print '==================================='
        print type(request.user)
        if getattr(obj,'add_user',None):
            obj.add_user=request.user.username
            print 'obj.add_user:',obj.add_user
            obj.save()


class SysLogsAdmin(admin.ModelAdmin):
    list_display = ['logs','errs','add_time']



admin.site.register(rep_queue,RepQueueAdmin)
admin.site.register(sys_logs,SysLogsAdmin)