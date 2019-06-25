# -*- coding:utf-8 -*-
# @Time     :2019/06/25  14:45
# @Author   :刘向上
# @File     :hijuu.py
# @explain  :用来现在hijuu国产区视频

import requests
import re
import socket
import time
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor


class hijuu:
    def __init__(self):
        self.url = 'http://hijuu.net/'  # 默认地址
        self.headers = {
            'User-Agent': 'JSBoxMain/335 CFNetwork/978.0.7 Darwin/18.6.0'
        }
        self.path = '/Users/pleasecallme/Documents/视频/m3u8/hijuu/'
        self.pool = ThreadPoolExecutor(max_workers=10)   # 最大线程数
        socket.setdefaulttimeout(10)    # 超时时间

    def get_page_detail(self):
        """获取第一页的信息"""
        # 因为请求后返回的数据乱码，所以这里先更改返回的格式
        res = requests.get(self.url + 'v1.html', self.headers).content.decode('utf-8')
        all_list = re.findall('<a href="(.*?)" title="(.*?)"', res)     # 获取详细地址以及标题
        for list in all_list:
            title = list[1]
            href = list[0]
            self.get_file_detail(href)
            cat_cmd = f'cat {self.path}/*.ts > {self.path}/{title}.ts'
            time.sleep(2)
            ffpmg_cmd = f'ffmpeg -y -i {self.path}/{title}.ts -c:v ' \
                f'libx264 -c:a copy -bsf:a aac_adtstoasc {self.path}/{title}.mp4'
            del_cmd = f'rm -f {self.path}/*.ts'
            os.system(cat_cmd)  # 复制文件
            print()
            time.sleep(2)
            os.system(ffpmg_cmd)  # hallo
            print()
            time.sleep(2)
            os.system(del_cmd)
            time.sleep(3)

    def get_file_detail(self, url):
        res = requests.get(self.url + url, self.headers).content.decode('utf-8')
        video_src = re.findall('<video src="(.*?)" controls', res)[0]
        self.get_m3u8_address_detail(video_src)

    def get_m3u8_address_detail(self, url):
        res = requests.get(url).text.split('\n')
        # print(res.text)
        index_list = []
        complete_list = []
        for i in res:
            if '.ts' in i:
                index_list.append(i)
        for index in index_list:
            complete_list.append(url.replace('index.m3u8', index))
        task = self.pool.map(self.download_for_multi_process, complete_list)
        for t in task:
            pass

    def download_for_multi_process(self, url):
        self.download_file(url)
        print(f'{url}   ---->   done!')

    def download_file(self, url):
        try:
            urllib.request.urlretrieve(url, self.path + url.split('/')[-1])
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.request.urlretrieve(url, self.path + url)
                    break
                except socket.timeout:
                    err_info = url+' Reloading for %d time'\
                               % count if count == 1 else 'Reloading for %d times' % count
                    print(err_info)
                    count += 1
                except:
                    self.download_file(url)
            if count > 5:
                print('download fialed!')
        except:
            self.download_file(url)

    def run(self):
        self.get_page_detail()


if __name__ == '__main__':
    run = hijuu()
    run.run()



