# -*- coding:utf-8 -*-
# @Time     :2019/06/14  17:39
# @Author   :刘向上
# @File     :cmd.py
# @Order    :



import os



cmd = 'cat /Users/pleasecallme/Documents/视频/m3u8/*.ts > /Users/pleasecallme/Documents/视频/m3u8/mp4/4.ts'
# os.system(cmd)

cmd1 = 'ffmpeg -y -i /Users/pleasecallme/Documents/视频/m3u8/3.ts -c:v libx264 -c:a copy -bsf:a aac_adtstoasc ' \
       '/Users/pleasecallme/Documents/视频/m3u8/3.mp4'
# os.system(cmd1)


dele_cmd = 'rm -f /Users/pleasecallme/Documents/视频/m3u8/*.ts'

os.system(dele_cmd)
