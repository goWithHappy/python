# import asyncio
# import sys
#
# from MyWebsite.www.AppTableModel import User
# from MyWebsite.www.orm import create_pool
#
#
# def test(loop):
#     yield from create_pool(loop=loop,user='root',password='19950903a',database='awesome')
#     u=User(name='test',email='text@163.com',passwd='123456',image='about.blank')
#     yield from u.save()
#
# loop=asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.close()
# #在loop.close()这句代码后，程序还会循环运行，所以导致了这个错误
# if loop.is_closed():
#     sys.exit(0)