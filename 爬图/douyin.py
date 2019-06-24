# -*- coding:utf-8 -*-
# @Time     :2019/06/18  14:20
# @Author   :刘向上
# @File     :douyin.py
# @Order    :爬取类似于抖音的豆奶视频
# @ps       :因为版本的原因，提示升级，等修改后在爬取

import requests
import json
import urllib3
import socket
import urllib.request
import time
import os
from concurrent.futures import ThreadPoolExecutor


class DouNai:
    def __init__(self):
        self.abs_file = __file__
        self.abs_file = self.abs_file[:self.abs_file.rfind('/')] + '/douyin'    # 当前路径
        self.pool = ThreadPoolExecutor(max_workers=10)  # 线程数，最大线程数为10
        socket.setdefaulttimeout(20)    # 设置超时时间

    def download_file(self, url, target):
        try:
            urllib.request.urlretrieve(url, target)
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.request.urlretrieve(url, target)
                    break
                except socket.timeout:
                    err_info = url+' Reloading for %d time'\
                               % count if count == 1 else 'Reloading for %d times' % count
                    print(err_info)
                    count += 1
                except:
                    self.download_file(url, target)
            if count > 5:
                print('download fialed!')
        except:
            self.download_file(url, target)

    def get_all_url(self):
        """先获取列表视频列表信息"""
        url = 'https://www.linhaotian3.cn/api/public/'
        d = {
            'service': 'Video.getRecommendVideos',
            'uid': '-9999',
            'type': 0,
            'isstart': 1,
            'p': 1
        }
        headers = {
            'User-Agent': 'iphoneLive/1.1.1 (iPhone; iOS 12.0; Scale/3.00)',
            'http_app_version': '1.1.1'
            # 'Content-Type': 'application/x-www-form-urlencoded'
        }
        urllib3.disable_warnings()  # 屏蔽https警告
        res = requests.post(
            url,
            headers=headers,
            params=d,
            verify=False  # 防止https报错
        ).text
        res_json = json.loads(res, encoding='utf-8')['data']['info']    # 列表
        print(res_json)
        # for i in range(len(res_json)):
        for i in range(len(res_json)):
            title = res_json[i]['title']    # 文件标题
            href = res_json[i]['href']  # 文件地址
            index_url = href.split('.m3u8')[0]
            if title == 'AG亚游':
                continue
            else:
                if index_url.endswith('index'):
                    continue
                else:
                    self.get_url_detail(href)
                    time.sleep(3)
                    cat_cmd = f'cat {self.abs_file}/*.ts > {self.abs_file}/{title}.ts'
                    ffpmg_cmd = f'ffmpeg -y -i {self.abs_file}/{title}.ts -c:v ' \
                        f'libx264 -c:a copy -bsf:a aac_adtstoasc {self.abs_file}/{title}.mp4'
                    del_cmd = f'rm -f {self.abs_file}/*.ts'
                    os.system(cat_cmd)  # 复制文件
                    print()
                    time.sleep(2)
                    os.system(ffpmg_cmd)    # hallo
                    print()
                    time.sleep(2)
                    os.system(del_cmd)

    def get_url_detail(self, url):
        """获取视频的详细信息"""
        # 拼接url地址，去除最后的.m3u8地址
        index_url = url.split('.m3u8')[0].split('/')
        http = ''
        for i in range(len(index_url)):
            if i == 0:
                htt = http + index_url[i] + '//'
            elif i == 1:
                pass
            elif 1 < i < len(index_url) - 1:
                htt = htt + index_url[i] + '/'
            elif i == len(index_url) - 1:
                pass
            elif i == len(index_url):
                pass
        index_url = htt
        urllib3.disable_warnings()
        res = requests.get(url, verify=False).text
        res_split = res.split('\n')
        index_m3u8_url = ''
        # 因为有的m3u8地址请求后，直接给到了.ts地址，有的还是给到的.m3u8地址，所以这里需要做一下判断
        if '.ts' in res:
            # 这样出来的ts地址有加密，暂时先不写破解方法，先去执行m3u8
            pass
        elif '.m3u8' in res:
            print(res)
            print()
            for n in range(len(res_split)):
                if '.m3u8' in res_split[n]:
                    index_m3u8_url = index_url + res_split[n]
            print(index_m3u8_url)
            print()
            self.get_ts_list(index_m3u8_url, index_url)

    def get_ts_list(self, url, index_url):
        """获取到所有ts文件"""
        if 'index.m3u8' in url:
            pass
        else:
            urllib3.disable_warnings()
            res = requests.get(url, verify=False).text
            res_split = res.split('\n')
            ts_list = []
            if 'EXT-X-ALLOW-CACHE:YES' not in res:
                # 有时候获取的文件加密，暂时先破解加密文件，先过
                pass
            else:
                for i in range(len(res_split)):
                    if '.ts' in res_split[i]:
                        ts_list.append(index_url + res_split[i])
            if len(ts_list) > 0:
                print(ts_list)
                task = self.pool.map(self.download_for_multi_process, ts_list)  # 非阻塞
                for t in task:  # 阻塞
                    pass

    def download_for_multi_process(self, url):
        """多线程下载文件"""
        # target = abs_file + url.split('.ts')[0].split('/')[-1] + '.ts'
        target = f'{self.abs_file}/{url.split(".ts")[0].split("/")[-1]}.ts'

        self.download_file(url, target)
        print(f'{url}   ---->   done!')

    def run(self):
        self.get_all_url()


if __name__ == '__main__':
    run = DouNai()
    run.run()
