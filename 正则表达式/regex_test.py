import re

# [1]文档中所有大写字母开头的单词
# [2]找到其中所有数字,整数,小数,正数负数,分数,百分数
# [3]将所有日期提取出来(2019-1-3),变为2019.1.3

pattern = r"\b[A-Z]\w+\b"
pattern2 = r"%?-?\d+/?\.?\d*"
pattern3 = r"\d+-\d+-\d+"
if __name__ == "__main__":
    with open("file",'rt') as fr:
        data = fr.read()
        print(data)
        # regex调用
        regex = re.compile(pattern2)


        l = regex.findall(str(data))
        # for _ in l:
        #     ned = ".".join(_.split("-"))
        #     print(ned)
        print(l)




