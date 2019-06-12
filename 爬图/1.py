# -*- coding:utf-8 -*-
# @Time     :2019/5/2 21:51    
# @Author   :刘向上
# @File     :1.py
# @Ordef    :m3u8下载

import requests
import datetime
import json
import xlrd
import xlwt
import urllib3
import urllib.request


class M3U8():
    def __init__(self):
        pass

    def open_workbook(self):
        workbook_name = 'm3u8'
        workbook_sheet = 'hallo'
        data = xlrd.open_workbook(f'{workbook_name}.xls')
        table = data.sheet_by_name(f'{workbook_sheet}')
        rows = table.nrows  # 获取Excel表格中的总行数
        for i in range(1, 2):
            '''从第二行数据开始读取'''
            videoName = table.row_values(i)[0]  # 视频名称
            videoUrl = table.row_values(i)[1]   # 视频地址
            print(videoUrl)
            self.trans_url(videoUrl)

    def trans_url(self, videoUrl):
        response = requests.get(videoUrl)
        print(response.text)
        with open('1.m3u8', 'w') as f:
            f.writelines(response.text)
            f.close()

        with open('1.m3u8', 'r') as f_read:
            read_f = f_read.readlines()
            for n in read_f:
                if '.m3u8' in n:
                    end_url = n
                    print(end_url)
            f_read.close()
        # 带有ts地址的url链接
        url_ts = videoUrl.split('/index.m3u8')[0] + '/' + end_url
        print(url_ts)
        self.get_ts(url_ts)

    def get_ts(self, url_ts):
        res = requests.get(url_ts)
        # 写入ts文件
        with open('1.m3u8', 'w') as f:
            f.writelines(res.text)
            f.close()

        with open('1.m3u8', 'r') as f_read:
            read_f = f_read.readlines()
            for rd_f in read_f:
                if '.ts' in rd_f:
                    print(rd_f.split('\n')[0])
            f_read.close()

    # def download_ts(self):




    def run(self):
        self.open_workbook()


if __name__ == '__main__':
    run = M3U8()
    run.run()

