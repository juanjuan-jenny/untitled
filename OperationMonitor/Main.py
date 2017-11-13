from OperationMonitor.SshConnect import sshConnect
from OperationMonitor.OperateFile import writeFile, readFile
from OperationMonitor.ConnectDB import connectDB
from OperationMonitor.MakeSQL import makeSQL
from OperationMonitor.GetDate import getYesterday
from OperationMonitor.GetDatalist import getDatalist

import types


if __name__ == '__main__':

    searchSQL = '''
        SELECT sar_ip_info.id,
            sar_ip_info.ip,
            sar_ip_info.connection,
            sar_ip_account.username,
            sar_ip_account.password
        FROM sar_ip_info
          LEFT JOIN sar_ip_account ON sar_ip_info. id =sar_ip_account.ip_id
        WHERE sar_ip_info.status =\'1\' AND sar_ip_account.status=\'1\'
    '''
    searchResults = connectDB(host='10.60.81.54',
                  port=3306,
                  username='op_db',
                  password='Gjs@1234',
                  dbname='gjs_db',
                  type='select',
                  exesql=searchSQL)

    hostID = host = user = passwd = type = ''

    yesterday = getYesterday()

    command = 'sar -r -f /var/log/sa/sa' + yesterday.strftime('%d') + ' | grep \'Average\' '

    for tmpResult in searchResults:
        hostID = tmpResult[0]
        host = tmpResult[1]
        type = tmpResult[2]
        user = tmpResult[3]
        passwd = tmpResult[4]
        # print ("hostID=%d,host=%s,user=%s,passwd=%s,type=%s" %(hostID,host,user,passwd,type))

        connectResult = sshConnect(hostname = host,
                        username = user,
                        password = passwd,
                        type = type,
                        command = command)
        # print(connectResult)



        # writeFile('test.txt',connectResult)
        # fileList = readFile('test.txt')

        sql = makeSQL(hostID,getDatalist(connectResult))

        connectDB(host='10.60.81.54',
                  port=3306,
                  username='op_db',
                  password='Gjs@1234',
                  dbname='gjs_db',
                  type='insert',
                  exesql=sql)



    # result = sshConnect(hostname='10.60.81.54',
    #                     username='qhntp',
    #                     password='/home/qhntp/.ssh/id_rsa', #'/home/qhntp/.ssh/id_rsa',
    #                     type='2',
    #                     command='sar -r -f /var/log/sa/sa10 | grep \'Average\' ')
    # print(type(result))


