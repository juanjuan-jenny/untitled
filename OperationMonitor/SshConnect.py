# -*- coding: utf-8 -*-
import paramiko,sys

#连接服务器，执行sql
#使用密码连接
def sshConnect(hostname,username,password,type,command):

    try:
        con = paramiko.SSHClient()
        con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if type == '1': #密码
            # print('password')
            con.connect(hostname=hostname, port=22, username=username, password=password)
        elif type == '2': #公钥
            # print('pkey')
            pkey = paramiko.RSAKey.from_private_key_file(password)
            con.connect(hostname=hostname, port=22, username=username, pkey=pkey)
        else:
            print('The password or key is null!')

        # for key in shell:
        # stdin,stdout,stderr = s.exec_command(shell[key])
        # result[key] = stdout.read(),stderr.read()

        stdin,stdout,stderr = con.exec_command(command)
        result = stdout.read().decode()

        # print(result)
        return result
    except Exception as e:
        return e
    finally:
        con.close()

#使用密钥连接
