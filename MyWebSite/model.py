#实现数据库中的表所对应的Model
import time,uuid
from MyWebSite.orm import Model, StringField, BooleanField, FloatField, TextField

#使用时间戳和uuid库中的函数来生成唯一的uuid码，相当于一个hash码
def next_id():
    return '%015%s000' %(int(time.time()*1000),uuid.uuid4().hex)

#用户表
class User(Model):
    __table__='users'

    #设置表的基本属性
    id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    email=StringField(ddl='varchar(50)')
    passwd=StringField(ddl='varchar(50)')
    admin=BooleanField()
    name=StringField(ddl='varchar(50)')
    image=StringField(ddl='varchar(500)') #存储的是图片的基本路径
    create_at=FloatField(default=time.time())

#博客内容表,暂时不支持发送带图片的内容表
class Blog(Model):
    __table__='blogs'

    #设置博客表的基本属性
    id=StringField(primary_key=True,default=next_id,ddl='varchar50')
    user_id=StringField(ddl='varchar(50)')
    user_name=StringField(ddl='varchar(50)')
    user_image=StringField(ddl='varchar(500)')
    user_name=StringField(ddl='varchar(50)')
    summary=StringField(ddl='varchar(200)')
    content=TextField()
    create_at=FloatField(default=time.time())

#评论表的基本内容
class Comment(Model):
    __table__='comment'

    #设置评论表的基本信息
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)
