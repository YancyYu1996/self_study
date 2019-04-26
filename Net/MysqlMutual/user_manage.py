# user_manage.py
# 订单管理类（业务逻辑层/控制层）
# 处理跟订单相关的逻辑操作，调用DAO来实现数据存取
from user import *
from userIfo_dao import *

class UserManage:
    def __init__(self):
        # 实例化数据访问对象
        self.userIfo_dao = user_dao()
    
    def query_all_user(self):
        # 做业务逻辑方面的处理，此处不需要做
        return self.userIfo_dao.query_all_user()
    def query_one_user(self,username):
        # 做业务逻辑方面的处理，此处不需要做
        return self.userIfo_dao.query_one_user(username)
    
    def add_user(self,username,passwd):
        msg = []
        msg.append(username)
        msg.append(passwd)
        return self.userIfo_dao.add_user(msg)
    
    def del_user(self,username):
        msg = []
        msg.append(username)
        return self.userIfo_dao.del_user(msg)
    
    def mod_msg(self,needMod,newContent,username):
        msg = []
        msg.append(needMod)
        msg.append(newContent)
        msg.append(username)
        return self.userIfo_dao.mod_msg(msg)
        
        
        
        
