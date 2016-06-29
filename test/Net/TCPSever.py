#创建服务器
import socket
import threading
import time
from concurrent.futures import thread

#首先创建一个基于IPv4
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#监听端口
s.bind(('localhost',8888))
s.listen(5)
print('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
def tcplink(sock,addr):
    print('accept new connection from %s:%s'%addr)
    sock.send(b'Welcome!')
while True:
    data=sock.recv(1024)
    time.sleep(1)
    if not data or data.decode('utf-8')=='exit':
        break
    sock.send(('Hello,%s'% data.decode('utf-8')).encode('utf-8'))
# 创建新线程来处理TCP连接:
t = threading.Thread(target=tcplink,args=(sock, addr))
t.start()
sock.close()
print('Connection from %s:%s closed'% addr)
