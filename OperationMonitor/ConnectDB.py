import pymysql,builtins

def connectDB(host,port,username,password,dbname,type,exesql):
    db = pymysql.connect(host=host,port=port,user=username,password=password,db=dbname)
    cursor = db.cursor()
    sql = exesql
    results = ()

    try:
        cursor.execute(sql)
        if type in ('insert', 'update', 'delete') :
            db.commit()
        elif type in ('select') :
            results = cursor.fetchall() #tuple

            # for row in results:
            #   id = row[0]
            #   ip = row[1]
            #   connection = row[2]
            #    # 打印结果
            #   print ("id=%s,ip=%s,connection=%s" % \
            #          (id, ip, connection))

    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()
        return results

