#coding:utf-8
#调度器
from apscheduler.schedulers.blocking import *
import MySQLdb
import logging
import paramiko

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='collectschd.log',
                filemode='w')


def GetQueueId():
    rows=()
    try:
        logging.info('connect to database')
        db=MySQLdb.connect(host='10.200.8.106',port=3306,user='root',passwd="simba2016",db='monidb')
        # logging.INFO('connect to database')
        c=db.cursor()
        c.execute("select src_ip,src_path,tgt_ip,tgt_path from rep_queue")
        rows=c.fetchall()
        # if len(rows)>0:
        #     for row in rows:
        #         print row[0]
    except Exception,e:
        logging.error(e)
    finally:
        db.close()
        logging.info('connection of database closed complete!')
    if len(rows)>0:
        for row in rows:
            print row[0]


schd=BlockingScheduler()
schd.add_job(GetQueueId,'interval',seconds=2)
schd.start()