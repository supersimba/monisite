#coding:utf-8

from django.db import models
import datetime
from django.contrib.auth.models import User,AbstractUser


class ReqQueueManager(models.Manager):
    def get_queryset(self):
        return super(ReqQueueManager,self).get_queryset().filter(rid=6)

class rep_queue(models.Model):
    rid=models.AutoField(primary_key=True)
    describe=models.CharField(max_length=100,blank=False,verbose_name=u'队列描述')
    src_ip=models.GenericIPAddressField(blank=False,verbose_name=u'源端IP')
    src_path=models.CharField(max_length=100,blank=False,verbose_name=u'源端路径')
    src_ssh_user=models.CharField(max_length=20,blank=False,verbose_name=u'源端ssh用户名')
    src_ssh_pwd = models.CharField(max_length=20, blank=False, verbose_name=u'源端ssh密码')
    tgt_ip=models.GenericIPAddressField(blank=False,verbose_name=u'目标端IP')
    tgt_path = models.CharField(max_length=100, blank=False, verbose_name=u'目标端路径')
    tgt_ssh_user = models.CharField(max_length=20, blank=False, verbose_name=u'目标端ssh用户名')
    tgt_ssh_pwd = models.CharField(max_length=20, blank=False, verbose_name=u'目标端ssh密码')
    add_user=models.CharField(max_length=50,blank=False,verbose_name=u'添加用户',default=u'---------')
    add_time=models.DateTimeField(verbose_name=u'信息添加时间',default=datetime.datetime.now)

    objects=models.Manager()
    req_queue_objects=ReqQueueManager()

    class Meta:
        db_table='rep_queue'
        verbose_name=u'队列配置表'
        verbose_name_plural=verbose_name


class sys_logs(models.Model):
    logs=models.CharField(max_length=1000,verbose_name=u'运维系统日志信息')
    errs=models.CharField(max_length=1000,verbose_name=u'运维系统日志报错信息')
    add_time=models.DateTimeField(verbose_name=u'日志添加时间',default=datetime.datetime.now)

    class Meta:
        db_table='sys_logs'
        verbose_name=u'系统日志表'
        verbose_name_plural=verbose_name