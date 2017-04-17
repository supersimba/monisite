#coding:utf-8

from django.db import models


class rep_queue(models.Model):
    rid=models.AutoField(primary_key=True)
    describe=models.CharField(max_length=100,blank=False,verbose_name=u'队列描述')
    src_ip=models.GenericIPAddressField(blank=False,verbose_name=u'源端IP')
    src_path=models.CharField(max_length=100,blank=False,verbose_name=u'源端路径')