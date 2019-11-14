# *_*coding:utf-8 *_*
import sys
import requests
import time
import mitmproxy
from mitmproxy import http
from mitmproxy import flow, proxy, controller, options
from mitmproxy.proxy.server import ProxyServer
import time

'''
程序运行
 mitmdump -s scripts.py
 mitmdump -s <python1.y> | python <python2.py>
'''
#https://api-litchi.jstv.com/nav/10002630?OrderIndex=0&channel=0&pagesize=20&gid=9c2ea19a3963&AppID=litchiV5&Sign=e3b261f567e71db23d8d329a0c573f26&TT=495074222
def response(flow):
    if 'https://api-litchi.jstv.com/v6s/nav'  in flow.request.url:
        data = flow.request.url
        print(f">>>{data}<<<")
