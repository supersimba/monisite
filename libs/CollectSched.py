#coding:utf-8
#调度器
from apscheduler.schedulers.blocking import *
import MySQLdb
import logging
import paramiko

from checkconfig import check_ssh_connect

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='collectschd.log',
                filemode='w')


def GetQueueId():
    rows=()
    try:
        logging.info('connect to database')
        db=MySQLdb.connect(host='10.200.8.106',port=3306,user='root',passwd="simba2016",db='monidb')
        c=db.cursor()
        c.execute("select src_ip,src_path,tgt_ip,tgt_path from rep_queue")
        rows=c.fetchall()
    except Exception,e:
        logging.error(e)
    finally:
        db.close()
        logging.info('connection of database closed complete!')
    if len(rows)>0:
        for row in rows:
            srcip=row[0]
            srcpath=row[1]
            tgtip=row[2]
            tgtpath=row[3]

            print 'check source ip:', srcip
            if check_ssh_connect(srcip)>0:
                print 'ssh connect to source ip success!'
            else:
                print 'ssh connect to source ip false!'

            print 'check target ip:', srcip
            if check_ssh_connect(tgtip) > 0:
                print 'ok'
            else:
                print 'no'



            # sshcli=paramiko.SSHClient()
            # sshcli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # try:
            #     sshcli.connect(srcip,22,"oracle","oracle")
            #     stdin,stdout,stderr=sshcli.exec_command("ls -d "+srcpath)
            #     stdoutlist=stdout.readlines()
            #     stderrlist=stderr.readlines()
            #     if stdoutlist:
            #         print stdoutlist
            #     if stderrlist:
            #         print srcpath+' is not existed!'
            # except Exception,e:
            #     print srcip+' can not connect...........'
            # finally:
            #     sshcli.close()



schd=BlockingScheduler()
schd.add_job(GetQueueId,'interval',seconds=2)
schd.start()