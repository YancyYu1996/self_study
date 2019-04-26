# db_helper.py
# 封装数据库的基本操作
# 连接数据库，关闭连接，执行查询，执行增删改
from db_conf import *
import pymysql

class db_helper:
    def __init___(self):
        self.db_conn = None
    
    def open_conn(self):
        try:
            self.db_conn = pymysql.connect(host,user,passwd,dbname)   #连接
        except Exception as e:
            print("连接数据库错误")
            print(e)
        else:
            print("连接数据库成功")

    def close_conn(self): #关闭数据库连接
        try:
            self.db_conn.close()   #关闭
        except Exception as e:
            print("关闭数据库错误")
            print(e)
        else:
            print("关闭数据库成功")
        
    def do_query(self,sql):  #执行查询，返回结果集
        try:
            cursor = self.db_conn.cursor()   #获取游标
            cursor.execute(sql)   # 执行SQL
            resaul = cursor.fetchall()  # 提取数据
            cursor.close()    # 关闭游标
            return resaul     # 返回查询结果
        except Exception as e:
            print("执行查询错误")
            print(e)
            return None     # 执行失败，返回空对象

    def do_update(self,sql):      #执行增删改，返回受影响笔数
        try:
            cursor = self.db_conn.cursor() # 获取游标
            result = cursor.execute(sql)  # 执行SQL
            self.db_conn.commit()    # 提交事务
            cursor.close()           # 关闭游标
            return result            # 返回受影响笔数
        except Exception as e:
            self.db_conn.rollback()  # 出错则回滚
            print("执行更新出错")
            print(e)
            return None

# 测试代码
# if __name__ == "__main__":
#     dbhelper = db_helper()     # 实例化一个对象
#     dbhelper.open_conn()       # 打开数据库连接

#     sql = "select_server.py * from user"
#     result= dbhelper.do_query(sql)   #执行查询
#     for row in result:
#         print(row)
#     sql = 'insert into user values("yanson","1000000")'
#     result= dbhelper.do_update(sql)   #执行查询
#     print(result)
#     sql = "select_server.py * from user"
#     result= dbhelper.do_query(sql)   #执行查询
#     for row in result:
#         print(row)

#     dbhelper.close_conn()            # 关闭数据库连接

