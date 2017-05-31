#coding:utf-8
from apscheduler.schedulers.blocking import *
import MySQLdb
import logging
import paramiko
import datetime


cli=paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    cli.connect("10.200.8.106", 22, "oracle", "oracle")
    print "sh "+"/u01/monisite"+"/src_collect.sh"
    #stdin, stdout, stderr = cli.exec_command("sh "+"/u01/monisite"+"/src_collect.sh "+"/u01/ss")
    stdin, stdout, stderr = cli.exec_command("sh "+"/u01/monisite/src_collect.sh")
    out = stdout.readlines()
    print stderr.readlines()
    print out
    err=stderr.readlines()
except Exception,e:
    print e
finally:
    cli.close()