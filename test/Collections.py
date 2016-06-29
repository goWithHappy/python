#测试常见容器的使用
from collections import namedtuple
Point=namedtuple('Point',['x','y']) #注意Point是一种新的数据类型
point=Point('1','2')
print(point.x)
print(point.y)
print('###############################')
print(isinstance(point,Point))  #判断队形的从属
print(isinstance(point,tuple))
print(isinstance(Point,tuple))
print('##############################')
from collections import deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
for i in q:
    print('deque的元素为：'+i)
print('****************************')
q.popleft()
for i in q:
    print('操作完成之后剩余元素：'+i)
print('***************************')
#测试deaultdict的使用
from collections import defaultdict
dd=defaultdict(lambda:'defaultValue')
dd['key1']='abc'
print(dd['key1'])
print(dd['other'])
print('*****************************')
#测试OrderDict
from collections import OrderedDict
d=dict([('a',1),('c',2),('b',3)])
print(d)
print(d['a'])
print(d['b'])
#测试counter（简单计数器，统计字符出现的个数）
from  collections import Counter
print('###########################')
c=Counter()             #注意其value值是统计的数字
for i in 'progremming':
    print(c[i])
print(c)