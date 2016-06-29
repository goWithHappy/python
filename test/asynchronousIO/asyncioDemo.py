#对异步I/O的基本测试使用
import asyncio
import threading


@asyncio.coroutine
def hello():
    print('Hello World!!(%s)'%threading.current_thread())
    #异步调用asyncio.sleep()
    r=yield from asyncio.sleep(3)
    print('Hello again!(%s)'%threading.current_thread())
#获取EventLoop：
loop=asyncio.get_event_loop()
#执行cotoutie
tasks=[hello(),hello()]
#当tasks有多个任务时，当一个task耗时时，它会跳过去去执行另一个task
loop.run_until_complete(asyncio.wait(tasks))
loop.close()