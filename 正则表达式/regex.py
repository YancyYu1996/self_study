import re

# pattern = r"(\w+):(\d+)"
# s = "yancy:1996 lili:1890"
#
# # re模块调用
# l = re.findall(pattern,s)
# print(l)

# # regex调用
# regex = re.compile(pattern)
# l = regex.findall(s,pos=0,endpos=145)
# print(l)
#
# # 分割字符串
# l = re.split(r"\s+","hello   world")
# print(l)
#
# l = re.sub(r"垃圾","**","玩的真垃圾,sas垃圾",1)
# print(l)
#
# pattern = r"\d+"
s = "2019/4/23/,海军70周年"
# it = re.finditer(pattern,s)
# # print(dir(next(it)))
# for i in it:
#     print(i.group())
#
# obj = re.fullmatch(r"\w+","My_name")
# print(obj.group())

obj = re.match(r"[A-Z]\w+","My_name Yancy")
print(obj.group())

# 匹配目标字符串第一处符合条件的内容
obj = re.search(r"\d+",s)
print(obj.group())