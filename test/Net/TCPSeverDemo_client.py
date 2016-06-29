#创建一个简单的TCP服务器
#创建一个基于IPv4和TCP协议的Socket：
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('localhost',8888))
#读取欢迎消息
print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()