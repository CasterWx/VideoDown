# !/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import os
import threading
import time
import json

header = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip",
    "Content-Type":"application/json",
    "Accept-Language":"zh-CN",
    "Referer":"https://space.bilibili.com/33717177/favlist?fid=732841077&ftype=create",
    "Origin":"https://space.bilibili.com",
    "Cookie":"_uuid=1DBA4F96-2E63-8488-DC25-B8623EFF40E773841infoc; buvid3=FE0D3174-E871-4A3E-877C-A4ED86E20523155831infoc; LIVE_BUVID=AUTO8515670521735348; sid=l765gx48; DedeUserID=33717177; DedeUserID__ckMd5=be4de02fd64f0e56; SESSDATA=cf65a5e0%2C1569644183%2Cc4de7381; bili_jct=1e8cdbb5755b4ecd0346761a121650f5; CURRENT_FNVAL=16; stardustvideo=1; rpdid=|(umY))|ukl~0J'ulY~uJm)kJ; UM_distinctid=16ce0e51cf0abc-02da63c2df0b4b-5373e62-1fa400-16ce0e51cf18d8; stardustpgcv=0606; im_notify_type_33717177=0; finger=b3372c5f; CURRENT_QUALITY=112; bp_t_offset_33717177=303733919604041416; CNZZDATA2724999=cnzz_eid%3D728697910-1567138054-https%253A%252F%252Ft.bilibili.com%252F%26ntime%3D1569560686",
    "Host":"space.bilibili.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

queue = []

# 寻找一个下载任务
def find_video(threadName, delay):
    av_id = queue.get()
    download_video(av_id)

# 下载视频
def download_video(av_id):
    os.system('you-get -o d:/vedio/ https://www.bilibili.com/video/av'+str(av_id))


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        download_video(self.threadID)


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
