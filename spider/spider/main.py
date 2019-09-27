# !/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import os
import threading
import time
import json
from trd.mythread import myThread

# 创建两个线程
def create_thread(res):
    thread = myThread(res['id'],res['title'],res['id'])
    thread.start()

i = 1
while 1 :
    url = 'https://api.bilibili.com/medialist/gateway/base/spaceDetail?media_id=88854277&pn='+ str(i) +'&ps=20&keyword=&order=mtime&type=0&tid=0&jsonp=jsonp'
    html = requests.get(url)
    i = i + 1
    print(html.text)
    res = json.loads(html.text)
    len_video = len(res['data']['medias'][0])
    for id in range(0,len_video):
        create_thread(res['data']['medias'][id])
