#!/usr/bin/env python3
# userIfo_dao.py
# 订单数据访问对象
# d:data a:access o:object
# 拼装各种SQL语句，调用DBHelper的对象
# 实现数据库的操作
from db_helper import *
from user import *
class user_dao:
    def __init__(self):   # 构造函数
        # 创建，持有DBHelper对象
        self.db_helper = db_helper()
        self.db_helper.open_conn()  # 打开连接
    
    #析构函数，对象销毁时使用
    def __del__(self):
        self.db_helper.close_conn()

    # 查询所有用户信息,返回订单对象的列表
    def query_all_user(self):
        sql = 'select * from user'
        user_list = []    #用户对象的列表
        # 执行查询
        result = self.db_helper.do_query(sql)
        if not result:
            print("查询结果为空")
            return None
        for row in result:
            username = row[0]
            userpw = row[1]
            user_list.append(user(username,userpw))
        return user_list
    def query_one_user(self,username):
        sql = "select * from user where username = '%s'"%(username)
        user_list = []    #用户对象的列表
        # 执行查询
        result = self.db_helper.do_query(sql)
        if not result:
            print("查询结果为空")
            return None
        for row in result:
            username = row[0]
            userpw = row[1]
            user_list.append(user(username,userpw))
        return user_list
    
    def add_user(self,msg):
        sql = "insert into user values('%s',%d)"%(msg[0],msg[1])
        # 执行增加
        result = self.db_helper.do_update(sql)
        return result
    
    def del_user(self,msg):
        sql = "delete from user where username = '%s'"%(msg[0])
        # 执行删除
        result = self.db_helper.do_update(sql)
        return result
    
    def mod_msg(self,msg):
        if msg[0] == "username":
            sql = "update user set username = '%s' where username = '%s'"%(msg[1],msg[2])
        elif msg[0] == "password":
            sql = "update user set password = %d where username = '%s'"%(msg[1],msg[2])
        result = self.db_helper.do_update(sql)
        return result
    

        
