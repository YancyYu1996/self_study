# -*- coding:utf-8 -*-
'''
使用multiprocessing创建两个子进程，
分别复制一个文件的上下两个部分到一个新的文件中。
'''
from multiprocessing import Process,Pipe
import time,os
# 获取文件大小
filepath = r"/home/tarena/test/Net/process/2.jpg"
Fow_filepath = r"/home/tarena/test/Net/process/top.jpg"
Last_filepath  = r"/home/tarena/test/Net/process/bot.jpg"
# 创建管道
fd1,fd2 = Pipe()
fd3,fd4 = Pipe()

size = os.path.getsize(filepath)
f = open(filepath,'rb')
# 复制上半部分
def top():
    #f = open(filepath,'rb')
    n = size//2
    with open(Fow_filepath,'wb') as fw:
        fw.write(f.read(n))
    #f.close()

#复制下半部分
def bot():
    #f.open(filepath,'rb')
    with open(Last_filepath,'wb') as fw:
        fw.write(f.read())
    #f.close()

t = Process(target = top)
b = Process(target = bot)   

t.start()
b.start()
t.join()
b.join()
f.close()








