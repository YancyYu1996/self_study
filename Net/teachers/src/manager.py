# manager.py
# 管理员，老师信息的增删改

class manager:

    def add(self,msg):
        try:
            self.id = int(input("请输入增加的老师信息：1.id") or "0")
            self.name = input("2.名字")
            self.sex = input("3.性别，M/F")
            self.age = input("4.年龄0-100")
            self.course = input("5.所教课程")
            assert 0< self.age <=100,"年龄超过范围"
        except Exception as e:
            print(e)
            return None
        else:
            msg[0] = self.id
            msg[1] = self.name
            msg[2] = self.sex
            msg[3] = self.age
            msg[4] = self.course
            return msg
    
    def delete(self,msg):
        try:
            self.id = int("请输入需要删除的ID")
        except Exception as e:
            print(e)
            return None
        else:
            teacher.count -= 1
        





