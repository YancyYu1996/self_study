from socket import *

# 创建tcp套接字
s = socket()
s.bind(("0.0.0.0",8032))
s.listen(5)

c,addr = s.accept()
data = c.recv(4096)
print(data)
c.send(b'hello yancy')

c.close()
s.close()