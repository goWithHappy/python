#使用UDP进行消息传输
import socket

#创建socket对象
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#对端口进行绑定
s.bind(('127.0.0.1',9999))
#创建socket时，SOCKET_GRAM制定了这个socket类型的UDP，绑定端口和TCP一样，但是不需要调用listen（）方法，而是直接接受任何客户端的数据
print('Bind UDP on 9999...')
    #接受数据
while True:
    data,addr=s.recvfrom(1024)
    print('Received from %s:%s'%addr)
    s.sendto(b'Hello,%s'%data,addr)
#recvfrom()方法返回数据和客户端的端口连接，这样服务器收到数据后，直接调用sendto（）就可以把数据发给客户端