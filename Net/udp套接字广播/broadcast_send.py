# broadcast_send.py
from socket import *
from time import sleep

# 目标地址
dest = ("localhost",11111)

s = socket(AF_INET,SOCK_DGRAM)
data = '''*****************************清明节快乐************************************
四月未拂杨柳絮
十里春风不如你
***********************************************************************************'''
# 设置可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,True)
while True:
    sleep(2)
    s.sendto(data.encode(),dest)