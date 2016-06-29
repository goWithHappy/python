#测试SQLlite的使用
import sqlite3

#创建connection对象
conn=sqlite3.connect('test.db')
#创建cursor
cursor=conn.cursor()
#执行一条SQL语句，创建user表
# cursor.execute('create table user(id VARCHAR(20) PRIMARY KEY ,_name VARCHAR(20))')
#插入数据
cursor.execute('insert into user(id,_name) VALUES (\'6\', \'Michael\')')
print(cursor.rowcount)  #打印出插入的条数
cursor.close()
#提交事务
conn.commit()
#关闭conn
conn.close()
#对查询进行操作
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('select * from user where id=?',('2',)) #用？可以来做占位符，对应一个list(只适用于sqllite)
#获取查询结果
values=cursor.fetchall()
print(values)           #注意返回的结果是一个元组
cursor.close()
conn.close()