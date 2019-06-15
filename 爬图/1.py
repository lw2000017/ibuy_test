# -*- coding:utf-8 -*-
# @Time     :2019/5/2 21:51    
# @Author   :刘向上
# @File     :1.py
# @Ordef    :m3u8下载

import requests
import xlrd
import os
import urllib.request
import socket
from concurrent.futures import ThreadPoolExecutor


class M3U8:
    def __init__(self):
        self.pool = ThreadPoolExecutor(max_workers=10)      # 10个线程池执行异步调用
        socket.setdefaulttimeout(20)    # 设置超时时间为20s

    def open_workbook(self):
        """打开excel"""
        workbook_name = 'm3u8'
        workbook_sheet = 'hallo'
        data = xlrd.open_workbook(f'{workbook_name}.xls')
        table = data.sheet_by_name(f'{workbook_sheet}')
        rows = table.nrows  # 获取Excel表格中的总行数
        for i in range(3, 4):
            '''从第二行数据开始读取'''
            videoName = table.row_values(i)[0]  # 视频名称
            videoUrl = table.row_values(i)[1]   # 视频地址
            # print(videoUrl)
            self.trans_url(videoUrl, videoName)
            # 复制文件
            cmd = f'cat /Users/pleasecallme/Documents/视频/m3u8/*.ts > ' \
                f'/Users/pleasecallme/Documents/视频/m3u8/mp4/{videoName}.ts'
            os.system(cmd)

            dele_cmd = 'rm -f /Users/pleasecallme/Documents/视频/m3u8/*.ts'
            os.system(dele_cmd)

            cmd1 = f'ffmpeg -y -i /Users/pleasecallme/Documents/视频/m3u8/mp4/{videoName}.ts -c:v ' \
                f'libx264 -c:a copy -bsf:a aac_adtstoasc ' \
                   f'/Users/pleasecallme/Documents/视频/m3u8/mp4/{videoName}.mp4'
            os.system(cmd1)



    def trans_url(self, videoUrl, videoName):
        """转换成为带有ts地址的m3u8地址"""
        response = requests.get(videoUrl)
        # print(response.text)
        with open('1.m3u8', 'w') as f:
            f.writelines(response.text)
            f.close()

        with open('1.m3u8', 'r') as f_read:
            read_f = f_read.readlines()
            for n in read_f:
                if '.m3u8' in n:
                    end_url = n
                    # print(end_url)
            f_read.close()
        # 带有ts地址的url链接
        url_ts = videoUrl.split('/index.m3u8')[0] + '/' + end_url
        # print(url_ts)
        self.get_ts(url_ts, videoName)

    def get_ts(self, url_ts, videoName):
        """获得ts地址"""
        res = requests.get(url_ts)
        # 写入ts文件
        with open('1.m3u8', 'w') as f:
            f.writelines(res.text)
            f.close()
        ts_url = []
        with open('1.m3u8', 'r') as f_read:
            read_f = f_read.readlines()
            for rd_f in read_f:
                if '.ts' in rd_f:
                    # print(rd_f.split('\n')[0])
                    ts_url.append(rd_f.split('\n')[0])
            f_read.close()
        print(f'此文件共有{len(ts_url)}个ts文件')
        self.split_join_ts(ts_url, url_ts, videoName)

    def split_join_ts(self, ts_url, url_ts, videoName):
        """拼接ts地址"""
        # last_ts_url = []
        with open('1.m3u8', 'w+') as f:
            for i in ts_url:
                url = url_ts.split('/index.m3u8')[0] + '/' + i
                f.writelines(url + '\n')
            f.close()
        self.download_with_multi_process(videoName)

    def download_with_multi_process(self, videoName):
        """多线程下载"""
        with open('1.m3u8', 'r') as f:
            last_ts_url = f.readlines()
            f.close()
        # print(target)
        # print(last_ts_url[0].split('\n')[0])
        task = self.pool.map(self.download_for_multi_process, last_ts_url, videoName)  # 此时非阻塞
        for t in task:  # 此时会变成阻塞
            pass

    def download_for_multi_process(self, last_ts_url, videoName):
        target = '/Users/pleasecallme/Documents/视频/m3u8/' + last_ts_url.split('\n')[0].split('hls/')[-1]
        filename = target.split('/m3u8/')[-1]
        self.download_file(last_ts_url, target)
        print(f'{filename} ---> done!')

    def download_file(self, url, target):
        """下载文件"""
        '''次数超过5次后不再下载，避免陷入死循环'''
        try:
            urllib.request.urlretrieve(url, target)
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    urllib.request.urlretrieve(url, target)
                    break
                except socket.timeout:  # 20秒内没有响应，则重新下载
                    err_info = url + ' Reloading for %d time' % \
                               count if count == 1 else 'Reloading for %d times' % count
                    print(err_info)
                    count += 1
                except:
                    # 解决远程主机关闭问题
                    self.download_file(url, target)
            if count > 5:
                print("downloading fialed!")
        except:
            # 解决远程主机关闭问题
            self.download_file(url, target)

    def run(self):
        self.open_workbook()



if __name__ == '__main__':
    run = M3U8()
    run.run()

