def consumer():
    r=''
    while True:
        n=yield r
        if not n:     #指的是n为空时会满足条件
            print('别执行过！！')
        print('Consumer onsuming %s..'%n)
        r='200 OK'
#注意在程序运行过程中prudece（）多次调用consumer（）函数
def produce(c):
    c.send(None)       #c.send(None)用于启动一个生成器，如果参数不传None的话会报错，
    n=0;               #但也只是用于启动生成器并不会调用yield,也就是说当执行send（None）从
    while n<5:        #produce转到consumer时只执行到yield的上一句
        n=n+1
        print('Profuctor producing %s'%n)
        r=c.send(n)
        print('[Producer] Consumer return:%s..'%r)
    c.close()
c=consumer()
produce(c)