import pymysql

#demo
# db = pymysql.connect("10.60.81.54","op_db","Gjs@1234","gjs_db")
# cursor = db.cursor() #创建游标对象
# cursor.execute("SELECT VERSION()") #执行SQL语句
# data = cursor.fetchone() #获取返回数据
# print ("Database version : %s " % data) #打印数据
# db.close()

db = pymysql.connect(host="10.60.81.54",
                     # port=3306,
                     user="op_db",
                     password="Gjs@1234",
                     db="gjs_db")
cursor = db.cursor()
#新建表
# sql_create = """
#     CREATE TABLE test (
#         id bigint(20) NOT NULL AUTO_INCREMENT,
#         date DATE DEFAULT NULL,
#         time DATE DEFAULT NULL,
#         memfree VARCHAR(50) DEFAULT NULL,
#         memused VARCHAR(50) DEFAULT NULL,
#         memused_percent decimal(16,4) DEFAULT NULL,
#         buffers VARCHAR(50) DEFAULT NULL,
#         cached VARCHAR(50) DEFAULT NULL,
#         commit VARCHAR(50) DEFAULT NULL,
#         commit_percent decimal(16,4) DEFAULT NULL,
#         insertedtime DATE DEFAULT NULL,
#         insertedby VARCHAR(20) DEFAULT NULL,
#         updatedtime DATE DEFAULT NULL,
#         updatedby VARCHAR(20) DEFAULT NULL,
#         PRIMARY KEY (id)
#     ) ENGINE=INNODB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8
#     """

#删除表
# sql_drop = """drop TABLE test"""

#插入数据
# sql_insert ="""   """


try:
    cursor.execute(sql_create)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
finally:
    db.close()

# select table_name,table_comment from information_schema.columns where table_schema = 'gjs_db' and table_name = 'user' ;
# select COLUMN_NAME,DATA_TYPE,COLUMN_DEFAULT,column_comment from information_schema.columns where table_schema = 'gjs_db' and table_name = 'user' ;