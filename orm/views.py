#coding:utf-8

from django.shortcuts import render,render_to_response
from django.http import HttpRequest,HttpResponse
import MySQLdb
import json
import datetime
from datetime import date

from orm.models import *


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime('%Y%m%d %H:%M:%S')
        elif isinstance(obj,date):
            return obj.strftime('%Y%m%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self,obj)


#ormmoni page
def ormmoni(req):
    info = []
    dbip = '10.200.8.106'
    dbuser = 'root'
    dbpwd = 'simba2016'
    dbobj = rep_queue.objects.all()
    return render_to_response('ormmoni.html', {'dblist': dbobj})

def display_replogs(req):
    print req.POST
    return render_to_response('ormlogs.html')

def display_target_info(req):
    rid=req.POST["rid"]
    if req.method=='POST':
        infos=tgt_moni_info.objects.filter(queue_id=rid)
        if infos:
            #print infos.order_by('-tid')[0].tid
            o=infos.order_by('-tid')[0]
            infodic={
                'ssh_status':o.tgt_ssh_status,
                'path_status':o.tgt_path_status,
                'script_status':o.script_path_status,
                'sync_status':o.sync_status,
                'active':o.active,
                'collect_cnt':o.collect_cnt,
                'collect_err':o.collect_err,
                'loader_s_cnt':o.loader_s_cnt,
                'loader_r_cnt':o.loader_r_cnt,
                'loader_s_p_cnt':o.loader_s_p_cnt,
                'loader_r_p_cnt':o.loader_r_p_cnt,
                'loader_rate':o.loader_rate,
                'loader_time':o.loader_time,
                'loader_err':o.loader_err,
                'add_time':o.add_time,
                'record_flag': '1'
            }
            info_json=json.dumps(infodic,cls=CJsonEncoder)
        else:
            infodic = {
                'ssh_status':'',
                'path_status':'',
                'script_status':'',
                'sync_status':'',
                'active':'',
                'collect_cnt':'',
                'collect_err':'',
                'loader_s_cnt':'',
                'loader_r_cnt':'',
                'loader_s_p_cnt':'',
                'loader_r_p_cnt':'',
                'loader_rate':'',
                'loader_time':'',
                'loader_err':'',
                'add_time':'',
                'record_flag': '-1'
            }
            info_json = json.dumps(infodic, cls=CJsonEncoder)
        return HttpResponse(info_json)


def display_source_info(req):
    rid = req.POST["rid"]
    if req.method=='POST':
        infos=src_moni_info.objects.filter(queue_id=rid)
        if infos:
            #print infos.order_by('-tid')[0].tid
            o=infos.order_by('-sid')[0]
            infodic={
                'ssh_status':o.src_ssh_status,
                'path_status':o.src_path_status,
                'script_status':o.script_path_status,
                'sync_status':o.sync_status,
                'active':o.active,
                'dbps_cnt':o.dbps_cnt,
                'capture_cnt':o.capture_cnt,
                'sender_cnt':o.sender_cnt,
                'capture_err':o.capture_err,
                'sender_err':o.sender_err,
                'add_time':o.add_time,
                'record_flag':'1'
            }
            info_json=json.dumps(infodic,cls=CJsonEncoder)
        else:
            infodic = {
                'ssh_status': '',
                'path_status': '',
                'script_status': '',
                'sync_status': '',
                'active': '',
                'dbps_cnt': '',
                'capture_cnt': '',
                'sender_cnt': '',
                'capture_err': '',
                'sender_err': '',
                'add_time': '',
                'record_flag': '-1'
            }
            info_json = json.dumps(infodic, cls=CJsonEncoder)
        return HttpResponse(info_json)