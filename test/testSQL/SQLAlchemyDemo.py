#测试SQLAlchemy的基本使用
#ORM技术的测试
from sqlalchemy.dialects.mysql.base import INTEGER
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base

#创建对象的基类（所有ORM对象的基类）
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

Base=declarative_base()
#定义user对象：
class User(Base):
    #表的名字
    __tablename__='user_table'
    #表的结构
    id=Column(INTEGER,primary_key=True)
    name=Column(String)
    password=Column(String)
#初始化数据库连接
engine=create_engine('mysql+mysqlconnector://root:19950903a@localhost:3306/test')
#创建DBSession类型
DBsession=sessionmaker(bind=engine)
#通过ORM向数据库中添加数据
session=DBsession()
#创建User对象
new_user=User(id=10,name='Bob',password='123456')
#添加Session
session.add(new_user)
#提交并保存到数据库中
session.commit()
#关闭session
session.close()
#通过ORM进行查询操作
session=DBsession()
#创建Query（）查询，filter，filter是where的条件，最后调用one（）返回唯一行，all（）返回所有行
user=session.query(User).filter(User.id==1).one()
#打印查询出来的结果
print('name:',user.name)
#关闭session连接
session.close()