import re

# 只匹配ascii字符
# regex = re.compile(r"\w+",flags= re.A)

# 匹配时忽略大小写
# regex = re.compile(r"[a-z]\w*,flags=re.I)
regex = re.compile(r"^.",flags=re.M)

s = '''dsdaaf 
才会
'''
l = regex.findall(s)
print(l)