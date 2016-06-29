#书写关于自己网站的App Model
import time
import uuid

from MyWebsite.www.orm import Model, StringField, BooleanField, FloatField, TextField


#当未传入主键时，通过该方法来生成主键
def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)
#在编写ORM时，给Field增加一个default参数可以让ORM自己填入缺省值，缺省值可以作为函数对象输入，在调用save（）时自动计算
class User(Model):
    __table__='users'
    id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    email=StringField(ddl='varchar(50)')
    passwd=StringField(ddl='varchar(50)')
    admin=BooleanField()
    name=StringField(ddl='varchar(50)')
    image=StringField(ddl='varchar(500)')
    created_at=FloatField(default=time.time())

class Blog(Model):
    __table__='blogs'

    id=StringField(primary_key=True,default=next_id(),ddl='varchar(50)')
    user_id=StringField('varchar(50)')
    #图片存储的知识路径
    user_image=StringField(ddl='varchar(500)')
    name=StringField(ddl='varchar(50)')
    summary=StringField(ddl='varchar(200)')
    #正文通过纯文本形式来实现
    content=TextField()
    created_at=FloatField(default=time.time())

class Comment(Model):
    __table__='comments'

    id=StringField(primary_key=True,default=next_id(),ddl='varchar(50)')
    blog_id=StringField(ddl='varchar(50)')
    user_id=StringField(ddl='varchar(50)')
    user_name=StringField(ddl='varchar(50)')
    user_image=StringField(ddl='varchar(500)')
    conten=TextField
    created_at=FloatField(default=time.time())


