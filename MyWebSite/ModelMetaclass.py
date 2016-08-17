#model的基类，通过该类可以自动建立起类和表之间的映射关系
import logging;
logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

class ModelMetaclass(type):

    def __new__(cls, name, bases,attrs):
        #排除Moadel类本身的属性
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        #获取table的名称便于建立对应的映射关系
        tableName=attrs.get('__table__',None) or name
        #打印出获得的表与相应类型的信息
        logging.info('found model:%s (table:%s)'%(name,tableName))
        #获取所有Field和主键名
        #先将对应的基本信息进行初始化
        mappings=dict()
        fields=[]
        primaryKey=None
        for k,v in attrs.items():
            if isinstance(v,Field):
                logging.info('found mapping:%s==>%s'%(k,v))
                mapings[k]=v




