#!/usr/bin/env python
import json
import paramiko

#连接服务器
def connect(host,username,password):
#    'this is use the paramiko connect the host,return conn'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
#        ssh.connect(host,username='root',allow_agent=True,look_for_keys=True)
        ssh.connect(host,username,password,allow_agent=True)
        return ssh
    except:
        return None

#获取设置的命令
def command(args,outpath):
#    'this is get the command the args to return the command'
    cmd = '%s %s' % (outpath,args)
    return cmd

#执行命令
def exec_commands(conn,cmd):
#    'this is use the conn to excute the cmd and return the results of excute the command'
    stdin,stdout,stderr = conn.exec_command(cmd)
    results=stdout.read()
    return results

#上传文件
def copy_moddule(conn,inpath,outpath):
#    'this is copy the module to the remote server'
    ftp = conn.open_sftp()
    ftp.put(inpath,outpath)
    ftp.close()
    return outpath

#得到执行结果
def excutor(host,outpath,args):
    conn = connect(host)
    if not conn:
        return [host,None]
    #exec_commands(conn,'chmod +x %s' % outpath)
    cmd =command(args,outpath)
    result = exec_commands(conn,cmd)
    result = json.dumps(result)
    return [host,result]


def copy_module(conn,inpath,outpath):
    'this is copy the module to the remote server'
    ftp = conn.open_sftp()
    ftp.put(inpath,outpath)
    ftp.close()
    return outpath

#########################
if __name__ == '__main__':
    print json.dumps(excutor('10.60.81.54','ls',' -l'),indent=4,sort_keys=True)
    print copy_module(connect('10.60.81.54'),'kel.txt','/root/kel.1.txt')
    exec_commands(connect('10.60.81.54'),'chmod +x %s' % '/root/kel.1.txt')

