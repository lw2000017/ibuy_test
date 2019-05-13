# -*- coding:utf-8 -*-          
# @Time     :2019/5/2 20:54    
# @Author   :LW                 
# @File     :123.py         


import urllib.request
import urllib.error
import os
import shutil
import datetime
import requests
import xlrd
import threading
import threading
# 创建一个多线程
class thread(threading.Thread):
    def run(self):
        getDown_requests()


# 请求最新的m3u8地址
def geturlData(url):
    try:
        urlData = urllib.request.urlopen(url, timeout=20)
        return urlData
    except Exception as err:
        print(f'err getUrlData {url}\n', err)
        return -1


def getDown_requests(url, file_path):
    try:
        start = datetime.datetime.now().replace(microsecond=0)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
        response = requests.get(url, headers)
        with open(file_path, mode='ab+') as f:
            f.write(response.content)
        end = datetime.datetime.now().replace(microsecond=0)
        # ts_name = file_path
    except Exception as e:
        print(e)

def getvideo_requests(url, path, videoName):
    print('begin run~ \n')
    urlData = geturlData(url)   # 请求新的m3u8地址，获取详细信息
    tempName_video = os.path.join(path, f'{videoName}.ts')  # 清空顺带创建tempName_video文件，防止中途停止，继续下载重复写入
    print(tempName_video)
    open(tempName_video, 'wb').close()      # 打开文件并写入数据，关闭
    url_ts = []
    for line in urlData:
        url_ts1 = str(line.decode('utf-8')).strip()      # strip()用来清除多余的空格和换行符
        if not '.ts' in url_ts1:
            continue
        else:
            if not url_ts1.startswith('http'):
                url_ts1 = url.replace(url.split('/')[-1], url_ts1)
                url_ts.append(url_ts1)
    print(url_ts)
    num = 0
    while num < len(url_ts):
        pass
        # getDown_requests()



if __name__ == '__main__':
    # workbook_name = 'm3u8'
    # workbook_sheet_name = 'hallo'
    # workbook = f'{workbook_name}.xls'
    # data = xlrd.open_workbook(workbook)
    # table = data.sheet_by_name(f'{workbook_sheet_name}')
    # rows = table.nrows  # 获取总行数
    # for i in range(1, rows):
        # 从第二行开始获取（第一行是标题）
    # videoName = table.row_values(i)[0]  # 文件标题
    videoName = '一个m3u8视频'
    # url_m3u8 = table.row_values(i)[1]    # m3u8地址
    url_m3u8 = 'https://cdn.zyw605.org/guochan/20180627/v3kt4Sem/index.m3u8'
    path = 'C:\\m3u8 download\download'
    m3u8_data = urllib.request.urlopen(url_m3u8, timeout=20)    # 因为地址的原因，需要先请求一遍地址，获取到新的m3u8地址
    # m3u8_url_list = []
    for line in m3u8_data:
        m3u8_url = line.decode('utf-8')
        if '.m3u8' in m3u8_url:
            m3u8_url = url_m3u8.replace(url_m3u8.split('/')[-1], m3u8_url)
            getvideo_requests(m3u8_url, path, videoName)
    print(f'Download !')
