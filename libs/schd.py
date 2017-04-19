#coding:utf-8
#调度器
from apscheduler.schedulers.blocking import *
from apscheduler.schedulers.background import BackgroundScheduler


def myjob():
    print '111'

schd=BackgroundScheduler()
schd.add_job(myjob,'interval',seconds=2)
schd.start()