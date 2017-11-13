# -*- coding: utf-8 -*-
import paramiko

def python_ssh(hostname,username,password,**shell):
    try:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # 用于允许连接不在known_hosts名单中的主机
        s.connect(hostname = hostname,username = username,password = password)
        result = {}
        for key in shell:
            stdin,stdout,stderr = s.exec_command(shell[key])
            result[key] = stdout.read(),stderr.read()
        s.close()
        return result
    except:
        result = "no"
        return result

print(python_ssh('10.60.81.54','qhntp','Gjs@1234',FREE='sar -r -f /var/log/sa/sa10 | grep -E \'Average|%\''))

