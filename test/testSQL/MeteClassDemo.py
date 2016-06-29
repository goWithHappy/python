
class ListMetacclass(type):
    #cls指的是当前创建的类的对象
    def __new__(cls, name, bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetacclass):
    pass
L=MyList()
L.add(1)
print(L)