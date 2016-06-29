#创建一个简单的MSGA（不支持多用户并发访问）

#创建一个服务器连接，IP地址为空，段号8000，处理函数为application
from wsgiref.simple_server import make_server
#创建响应函数
def application(environ, start_resopnse):
    start_resopnse('200 OK',[('Content-Type','text/html')])
    return [b'<h1>Hello,web</h1>']

httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')
#开始监听http请求
httpd.serve_forever()