# user_manage_ui.py
# (UI:User Interface,用户接口)
# 订单管理程序用户接口层（视图层，View）
# 接收用户指令。显示执行结果
from user import *
from user_manage import *

User_Manage = None  # 订单管理对象，全局变量

def print_menu():   # 打印主菜单
    menu = '''---------------订单管理程序-----------------
    1 - 查询所有用户
    2 - 根据用户名查询密码
    3 - 新增用户
    4 - 修改用户密码
    5 - 删除订单
    其他 - 退出  '''
    print(menu)

def query_all():
    user_list = User_Manage.query_all_user() 
    if user_list:
        for _ in user_list:
            print(_)
def query_one():
    username = input("输入用户名")
    user_list = User_Manage.query_one_user(username) 
    if user_list:
        for _ in user_list:
            print(_)
def add_user():
    username = input("需要增加的用户")
    passwd   = int(input("增加的密码"))
    User_Manage.add_user(username,passwd)
def mod_msg():
    username = input("需要修改的用户名")
    print("1.修改用户名  2.修改用户密码")   
    while True:
        key = input()
        if key == "1":
            needMod = "username"
            newContent = input("输入新的的用户名")
            break
        elif key == "2":
            needMod = "password"
            newContent = int(input("输入新的的密码"))
            break
    User_Manage.mod_msg(needMod,newContent,username)

def del_user():
    username = input("需要删除的用户名")
    User_Manage.del_user(username)



if __name__ == "__main__":
    #global User_Manage
    User_Manage = UserManage()  # 实例化UserManage
    while True:
        print_menu()
        oper = input("请选择要执行的操作：")
        if oper == "1":   # 查询所有用户
            query_all()
        elif oper == "2": # 根据用户名查询密码
            query_one()

            
        elif oper == "3": # 新增用户
            add_user()
            
            
        elif oper == "4": # 修改用户密码
            mod_msg()
            
            
        elif oper == "5": # 删除订单
            del_user()
        else:
            break
