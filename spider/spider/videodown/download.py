import os

# 下载视频
def download_video(av_id):
    os.system('you-get -o d:/vedio/ https://www.bilibili.com/video/av'+str(av_id))

