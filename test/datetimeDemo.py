from datetime import datetime,timedelta

#测试datatime的使用
now =datetime.now()
print(now)
print(type(now))
#datatime转换timestamp
print('datetime转换之后的结果为'+str(now.timestamp()))
#timestamp转换datatime
time=now.timestamp()
print('timestamp转换之后的结果为'+str(datetime.fromtimestamp(time)))
#用datatime的构造方法来构造datatime对象
mydate=datetime(2016,4,14,12,20)
print(mydate)
#utc时间转换(即格林威治标准时间)
print('########################################')
print(datetime.utcfromtimestamp(mydate.timestamp()))
#str转换为datatime
strDate=datetime.strptime('2016--4--14 21:58:10','%Y--%m--%d %H:%M:%S')
print('##########################################')
print(strDate)
#datatime加减法
print('#######################################')
print('现在时间是'+str(now))
print('计算之后的时间为：'+str(now+timedelta(hours=10)))
