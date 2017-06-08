#coding:utf-8
import paramiko


class logviewer():
    def __init__(self,ip,path,sshuser,sshpwd,logfile):
        self.ip=ip
        self.filepath=path+'/log/'+logfile
        self.sshuser=sshuser
        self.sshpwd=sshpwd
        self.result=''
        #文件是否存在 1 存在 0 不存在 如果SSH不通，则=-1
        self.check_file_flag=0
    def check_file(self):
        sshcli=paramiko.SSHClient()
        sshcli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            sshcli.connect(self.ip, 22, self.sshuser, self.sshpwd)
            stdin, stdout, stderr = sshcli.exec_command('ls -lrt '+self.filepath)
            if stdout:
                self.check_file_flag=1
            else:
                self.check_file_flag=0
        except Exception, e:
            print e
            self.check_file_flag=-1
        finally:
            return self.check_file_flag
            sshcli.close()


    def ssh_connect(self):
        cli=paramiko.SSHClient()