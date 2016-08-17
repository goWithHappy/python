#整个程序运行的入口，是整个程序的骨架

#设定消息级别为INFO
import logging;
logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>basic app</h1>')

@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('Get','/',index)
    srv=yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info("服务已经开启：http://127.0.0.1:9000")
    return srv;

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()