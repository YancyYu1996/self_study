# order.py
# 订单类：存放用户信息的属性
class user:
    def __init__(self,username,userpw):
        self.username = username
        self.userpw = userpw
    

    def __str__(self):
        ret = "用户：%s,密码:%s"%(self.username,self.userpw)
        return ret
