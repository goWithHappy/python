import mysql.connector

#创建connector对象
conn=mysql.connector.connect(user='root',password='19950903a',database='test')
#创建cursor对象
cursor=conn.cursor()
#进行数据库操作
cursor.execute('select * from ceshi')
values=cursor.fetchall()
#打印出查询结果
print(values)
cursor.close()
conn.close()
#在执行完插入等操作后，应定要注意进行事物的提交
#Mysql的sql占位符为%s
