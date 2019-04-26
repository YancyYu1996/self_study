# -*- coding: utf-8 -*-
import sys
sys.path.append(r"/home/tarena/test/Net/tcp简单服务")
from tcp_client import *
import struct

st = struct.Struct('i32sif')
# 收发消息
if __name__ == "__main__":
    a = CreateSocket()
    while True:
        id = input("id>>")
        name = input("name>>")
        age = input("age>>")
        score = input("score>>")
        data = st.pack(int(id),name.encode(),int(age),float(score))
        a.sendData(data)

        data = a.ReceveData()  
        
        print("From server :",data.decode())
        print("Send message END")
        
    else:
        a.clientclose()