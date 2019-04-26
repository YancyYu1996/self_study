# -*- coding: utf-8 -*-
import sys

sys.path.append(r"/home/tarena/test/Net/tcp简单服务")
sys.path.append(r"/home/tarena/test/Net/MysqlMutual")
from tcp_server import *
from user_manage import *
import struct
st = struct.Struct('i32sif')
if __name__ == "__main__":
    b = CreateSocket()  
    
    while True:
        try:
            b.saccept()
        except Exception as e:
            print("error")
            break
        while True:       
            try:
                data = b.ResvData()
                data_list = st.unpack(data)
                print("message%d %s %d %f from"%(data_list[0],data_list[1].decode(),data_list[2],data_list[3]))
                User_Manage = UserManage()  # 实例化UserManage
                User_Manage.add_user(",".join(data_list),34)
                b.SendData("message resv ok")
            except Exception as e:
                print("客户端已经关闭")           
                b.CloseServer()                                                                  
                break
    b.CloseServerdeep()
    
