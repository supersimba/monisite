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
    tgt_ip=models.GenericIPAddressField(blank=False,verbose_name=u'目标端IP')
    tgt_path = models.CharField(max_length=100, blank=False, verbose_name=u'目标端路径')
    add_user=models.CharField(max_length=50,blank=False,verbose_name=u'添加用户',default=u'---------')
    # add_user=models.ForeignKey(User)
    add_time=models.DateTimeField(verbose_name=u'信息添加时间',default=datetime.datetime.now)

    objects=models.Manager()
    req_queue_objects=ReqQueueManager()

    class Meta:
        db_table='rep_queue'
        verbose_name=u'队列配置表'
        verbose_name_plural=verbose_name