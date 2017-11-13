# -*- coding: utf-8 -*-

#组装SQL
def makeSQL(hostID, arrayList):
    sql = '''INSERT INTO sar_memory_average (ip_id, infodate, insertedtime,insertedby, updatedtime, updatedby, memfree, memused, memused_percent, buffers, cached, commit, commit_percent) VALUES'''
    ip = hostID
    if (arrayList,list):
        i = 0
        temp = ''
        while i < len(arrayList) : #行
            sqltmp1 = ''
            # sqltmp2 = '(' + str(ip) + ''',DATE_SUB(CURDATE(),INTERVAL 1 DAY),CURTIME(), NOW(),'admin',NOW(),'admin','''
            sqltmp2 = '(' + str(ip) + ''',DATE_SUB(CURDATE(),INTERVAL 1 DAY), NOW(),'admin',NOW(),'admin','''
            # print('sqltmp2=',sqltmp2)
            for temp in arrayList[i] :
                if isinstance(temp,str):
                    sqltmp1 = sqltmp1 + '\''+ temp +'\','
                else:
                    print('It is not string!')

            sqltmp2 = sqltmp2 + sqltmp1[:-1] + '),'
            # print(sqltmp2)
            sql = sql + sqltmp2
            # print(sql)
            i = i + 1
    else:
        print('The parameters is not error!')
    sql = sql[:-1]
    # print(sql)
    return (sql)

# def getIpAccoount():
#     sql = '''select id, ip, connection from sar_ip_info where status='1' '''


