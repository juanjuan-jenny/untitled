#!/usr/bin/python3
# -*- coding: utf-8 -*-

#连接服务器执行命令
import paramiko,os,builtins,pymysql
# import json

def sshConnect(hostname,username,password,type,command):
    try:
        con = paramiko.SSHClient()
        con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if type == '1': #密码
            print('密码')
            con.connect(hostname=hostname, port=22, username=username, password=password)
        elif type == '2': #公钥
            print('获取公钥')
            pkey = paramiko.RSAKey.from_private_key_file(password)
            con.connect(hostname=hostname, port=22, username=username, pkey=pkey)
        else:
            print('密码或密钥为空。')

        # for key in shell:
        # stdin,stdout,stderr = s.exec_command(shell[key])
        # result[key] = stdout.read(),stderr.read()

        stdin,stdout,stderr = con.exec_command(command)
        # result = stdout.read().decode()

        result = {}
        result = stdout.read().decode()

        print(result)
        return result
    except Exception as e:
        return e
    finally:
        con.close()


#写入文件
def writeFile(filename,content):
    document = open(filename, 'w+')
    # print('文件名: ', document.name)
    document.write(content)
    # print(document.tell())
    #输出当前指针位置
    # document.seek(os.SEEK_SET)
    #设置指针回到文件最初
    # con = document.read()
    # print(con)
    document.close()

#读取文件，返回list
def readFile(filename):
    datalist = []

    with open(filename, 'rt') as handle:
        datas = [ln.strip('\n').split(' ') for ln in handle]
        # print(datas)

        i = 0

        for temp1 in datas:
            datalist.append([])
            if isinstance(temp1,list):
                for temp2 in temp1:
                    if temp2 == '' or temp2 is None or temp2 == 'Average:':
                        continue
                    else:
                        datalist[i].append(temp2)
                i = i + 1
            else:
                print('It is not list!')
    handle.close()
    # print(datalist)
    #[['1139255', '915273', '44.55', '148870', '624811', '92780', '0.89'], ['113925', '915273', '44.55', '148870', '624811', '92780', '0.89']]
    return datalist

#组装SQL
def makeSQL(arrayList):
    sqlList = []
    if (arrayList,list):
        i = 0
        temp = ''
        while i < len(arrayList) : #行
            tempSql = sql = ''
            for temp in arrayList[i] :
                if isinstance(temp,str):
                    tempSql = tempSql + '\''+ temp +'\','
                else:
                    print('It is not string!')

            sql = sql + '''INSERT INTO sar_memory_info (date, time, insertedtime,insertedby, updatedtime, updatedby, memfree, memused, memused_percent, buffers, cached, commit, commit_percent) \
                VALUES(DATE_SUB(CURDATE(),INTERVAL 1 DAY),CURTIME(), NOW(),'admin' ,NOW(),'admin','''

            sql = sql + tempSql[:-1] + ')'
            # print(sql)
            sqlList.append(sql)
            i = i + 1
    else:
        print('The parameters is not error!')
    # print(sqlList)
    return (sqlList)






#连接MySQL数据库,操作数据库
def connectDB(host,port,username,password,dbname,exesql):
    # db = pymysql.connect(host='10.60.81.54',
    #                      port=3306,
    #                      user='op_db',
    #                      password='Gjs@1234',
    #                      db='gjs_db')
    db = pymysql.connect(host=host,port=port,user=username,password=password,db=dbname)
    cursor = db.cursor()

    sql = exesql

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()

if __name__ == '__main__':
    result = sshConnect(hostname='10.60.81.54',
                        username='qhntp',
                        password='Gjs@1234',
                        type='1',
                        command='sar -r -f /var/log/sa/sa10 | grep \'Average\' ')

    # result = sshConnect(hostname='10.60.81.54',
    #                     username='qhntp',
    #                     password='/home/qhntp/.ssh/id_rsa', #'/home/qhntp/.ssh/id_rsa',
    #                     type='2',
    #                     command='sar -r -f /var/log/sa/sa10 | grep \'Average\' ')
    # print(type(result))

    writeFile('test.txt',result)
    # print('write end')

    fileList = readFile('test.txt')
    # print(fileList)

    list = makeSQL(fileList)
    # print(list)

    rows = len(list)
    # print(rows)

    i = 0

    while i < rows :
        # print(list[i])
        connectDB(host='10.60.81.54',
                  port=3306,
                  username='op_db',
                  password='Gjs@1234',
                  dbname='gjs_db',
                  exesql=list[i])
        i = i + 1
