#coding:utf-8
import paramiko


#run_flag:操作类型 0 执行check;1 startup;2 stop
class SyncOper():
    def __init__(self,ip,path,ssh_u,ssh_p,run_flag):
        self.ip=ip
        self.path=path
        self.ssh_u=ssh_u
        self.ssh_p=ssh_p
        self.run_flag=run_flag
        self.result=''

    def runcmd(self):
        if self.run_flag == '0':
            print 'begin to run cmd of check'
            cli = paramiko.SSHClient()
            cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                cli.connect(self.ip,22,self.ssh_u,self.ssh_p)
                stdin, stdout, stderr = cli.exec_command("sh " + self.path + "/scripts/check")
                if stdout.readlines():
                    for item in stdout.readlines():
                        self.result=self.result+item.replace('\n','<br />')
                if stderr.readlines():
                    for item in stderr.readlines():
                        self.result=self.result+item.replace('\n','<br />')
            except Exception,e:
                print e
                self.result=e
            finally:
                return self.result
        if self.run_flag == '1':
            print 'begin to run cmd of startup'
            cli = paramiko.SSHClient()
            cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                cli.connect(self.ip,22,self.ssh_u,self.ssh_p)
                stdin, stdout, stderr = cli.exec_command("sh " + self.path + "/scripts/start_vagentd")
                if stdout.readlines():
                    for item in stdout.readlines():
                        self.result=self.result+item.replace('\n','<br />')
                if stderr.readlines():
                    for item in stderr.readlines():
                        self.result=self.result+item.replace('\n','<br />')
            except Exception,e:
                print e
                self.result=e
            finally:
                return self.result
        if self.run_flag == '2':
            print 'begin to run cmd of stop'
            cli = paramiko.SSHClient()
            cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                cli.connect(self.ip,22,self.ssh_u,self.ssh_p)
                stdin, stdout, stderr = cli.exec_command("sh " + self.path + "/scripts/stop_vagentd")
                if stdout.readlines():
                    for item in stdout.readlines():
                        self.result=self.result+item.replace('\n','<br />')
                if stderr.readlines():
                    for item in stderr.readlines():
                        self.result=self.result+item.replace('\n','<br />')
            except Exception,e:
                print e
                self.result=e
            finally:
                return self.result



    def check_pro(self):
        pass