#测试TCP客户端的基本使用
import socket
#创建一个socket对象
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #第一个参数指定了所用的协议族，第二个参数指定所用的协议
s.connect(('www(first).sina.com',80))      #参数时个tuple包含地址和端口号
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www(first).sina.com.cn\r\nConnection: close\r\n\r\n')
#接受数据
buffer=[]
while True:
    d=s.recv(1024)          #接受数据时调用recv（max），一次最多指定的字节数，因此
    if d:                   #在一个while循环中反复接受，直到recv（）返回一个空数据
        buffer.append(d)    #表示接受完毕退出循环
    else:
        break
data=b''.join(buffer)
#关闭连接
s.close()
#将HTTP头和网页本身分离，把HTTP头打印出来，网页内容保存到文件中：
header,html=data.split(b'\r\n\r\n',1)#第二个参数‘1’，最多分成'1'+1个部分
print(header)
with open('sina.html','wb') as f:
    f.write(html)