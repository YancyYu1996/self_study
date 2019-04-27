from db_helper import *
dbhelper = db_helper()
dbhelper.open_conn()
def add_dict(msg):
    sql = 'insert into words (word,mean) values("%s","%s")' % (msg[0],msg[1])
    # 执行增加
    result = dbhelper.do_update(sql)
    return result

with open("dict.txt","rt") as fr:
    i = 0
    while True:
        msg = []
        data = fr.readline()
        msg.append(data[0:17].strip())
        msg.append(data[17:])
        add_dict(msg)
        print(msg[0])
        print(msg[1])
        if not data:
            break
