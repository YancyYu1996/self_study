from pymongo import MongoClient
import bson.binary

conn = MongoClient("localhost",27017)
db = conn.images
myset = db.ig

# # 存储图片
# with open("timg.jpeg","rb") as fr:
#     data = fr.read()
#
# # 将data转换为bson格式
# content = bson.binary.Binary(data)
#
# # 插入到集合
# dic = {"filename":"ig.jpeg","data":content}
# myset.insert_one(dic)

# 提取文件
img = myset.find_one({"filename":"ig.jpeg"})
with open("ig.jpeg","wb") as fw:
    fw.write(img["data"])

conn.close()

print()
