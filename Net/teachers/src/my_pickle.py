# my_pickle.py
# 文件的读写操作

import sys
sys.path.append("..")
from teachers.config import settings 

class my_pickle:
    @staticmethod
    def ReadMsg():
        # 创建文件流对象
        with open(settings.path+'/db/teacher_info.txt',"rt") as fr:
            for line in fr:
                print(line)

    @staticmethod
    def Delmsg(l):
        with open(settings.path+'/db/teacher_info.txt',"wt") as fw:
            for line in fw:
                fw_list = line.split(",")
                if fw_list[0] == l:
                    continue
                fw.write(line)
    
    @staticmethod
    def Modifymsg(l,n,so):
        with open(settings.path+'/db/teacher_info.txt',"wt") as fm:
            for line in fw:
                fw_list = line.split(",")
                if fw_list[0] == l:
                    fw_list[n]=so
                    line = ",".join(fw_list)
                fw.write(line)

    @staticmethod
    def Addmsg(msg):
        with open(settings.path+'/db/teacher_info.txt',"at") as fa:
            line = ",".join(msg)
            fa.write(line)


print(my_pickle.ReadMsg())


