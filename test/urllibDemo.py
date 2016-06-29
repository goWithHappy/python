#!/usr/bin/env python
#_*_coding=utf-8_*_
#测试url的使用
import urllib.request
#通过一般的IO进行操作
url="http://61.167.120.8/Index.html"
response=urllib.request.urlopen(url)
response.getcode()