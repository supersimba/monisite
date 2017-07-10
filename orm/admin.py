#coding:utf-8
from django.contrib import admin
from orm.models import *
# Register your models here.


class RepQueueAdmin(admin.ModelAdmin):
    list_display = ['describe','src_ip','src_path','tgt_ip','tgt_path', 'add_user','src_script_path','tgt_script_path','add_time']
    # list_editable = ['describe','src_ip','src_path','tgt_ip','tgt_path', 'add_time']
    def save_model(self, request, obj, form, change):
        print type(request.user)
        if getattr(obj,'add_user',None):
            obj.add_user=request.user.username
            print 'obj.add_user:',obj.add_user
            obj.save()
    def get_queryset(self, request):
        qs=super(RepQueueAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(add_user=request.user)


class SysLogsAdmin(admin.ModelAdmin):
    list_display = ['logs','errs','add_time']



admin.site.register(rep_queue,RepQueueAdmin)
admin.site.register(sys_logs,SysLogsAdmin)