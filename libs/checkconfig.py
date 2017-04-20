#coding:utf-8
#检查ssh连通性,及目录是否存在,文件是否存在
import sys
import paramiko
import os


def check_dir_exists():
    pass


def check_ssh_connect(sship):
    cli=paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cli.connect(sship, 22, "oracle", "oracle")
        return 1
    except:
        return 0
    finally:
        cli.close()