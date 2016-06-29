#通过一个元类书写一个ORM框架
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
	# 定义Model的元类
class StringField(Field):
    def __init__(self,name):
        super(StringField, self).__init__(name,'varchar(100)')
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField, self).__init__(name,'bigint')
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            # 判断如果是基类直接调用，直接返回不用判断
            return type.__new__(cls, name, bases, attrs)
        print('Found Model ')
        mappings = dict()
        for k, v in attrs.items():
            # 打印出得到的属性：
            print('得到的属性有：%s-->%s' % (k, v))
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)  # 删除已经保存到mapping中的Field属性
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 保存表的名称
        return type.__new__(cls, name, bases, attrs)
#定义基类model通过Metaclass来生成类的部分实体
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model, self).__init__(**kw)    #如果用户多输入了dict，就把它当做基本地dict属性

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'''Model object has no attribute %s''' % key)
    def __setattr__(self, key, value):
         self[key]=value

    #创建一个save方法将数据对象写入到数据库中
    def save(self):
        fields=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        #生成sql语句
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('sql:%s'%sql)
        print('ARGS:%s'%str(args))
class User(Model):
    #定义类的属性到列的映射
    id=IntegerField('id')
    name=StringField('name')
    email=StringField('email')
    password=StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
