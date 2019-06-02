# -*- coding:utf-8 -*-          
# @Time     :2019/5/5 15:01    
# @Author   :LW                 
# @File     :last_one.py         

import urllib.request
import urllib.error
import os
import shutil
import datetime
import requests
import xlrd


def getUrlData(url):
    try:
        urlData = urllib.request.urlopen(url, timeout=20)
        return urlData
    except Exception as err:
        print(f'err getUrlData {url}\n', err)
        return -1


# 下载文件
def getDown_reqursts(url, file_path):
    try:
        start = datetime.datetime.now().replace(microsecond=0)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
        response = requests.get(url, headers=headers)
        with open(file_path, mode='ab+') as f:
            f.write(response.content)
        end = datetime.datetime.now().replace(microsecond=0)
        ts_name = file_path.split('\\')[-1].split('.ts')[0]
        print(f'{ts_name}  -- > 下载耗时 {end-start}')
        print('down successful!\n')
    except Exception as e:
        print(e)


def getVideo_requests(url, path, videoName):
    print('begin run~\n')
    urlData = getUrlData(url)
    tempName_video = os.path.join(path, f'{videoName}.ts')
    open(tempName_video, 'wb').close()      # 清空顺带创建tempName_video文件，防止中途停止，继续下载重复写入
    for line in urlData:
        url_ts = str(line.decode('utf-8')).strip()      # strip(), 用来清除字符串前后存在的空格符和换行符
        if not '.ts' in url_ts:
            continue
        else:
            if not url_ts.startswith('http'):       # 判断是否以http开头，不是则需要拼接
                url_ts = url.replace(url.split('/')[-1], url_ts)
        # print(url_ts)
        getDown_reqursts(url=url_ts, file_path=tempName_video)  # 下载视频流
    filename = os.path.join(path, f'{videoName}.mp4')
    shutil.move(tempName_video, filename)
    print(f'Great, {videoName}.mp4 finish down!')


if __name__ == '__main__':
    workbook_name = '网红'
    workbook_sheet_name = 'Sheet1'
    workbook = f'{workbook_name}.xls'
    data = xlrd.open_workbook(workbook)
    table = data.sheet_by_name(f'{workbook_sheet_name}')
    rows = table.nrows  # 获取总行数
    for i in range(1, rows):
        # 从第二行开始获取（第一行是标题）
        videoName = table.row_values(i)[0]  # 文件标题
        url_m3u8 = table.row_values(i)[1]    # m3u8地址
        path = 'C:\\Downloads'
        m3u8_data = urllib.request.urlopen(url_m3u8, timeout=20)    # 因为地址的原因，需要先请求一遍地址，获取到新的m3u8地址
        # print(m3u8_data)
        for line in m3u8_data:
            m3u8_url = line.decode('utf-8')
            if '.m3u8' in m3u8_url:
                # print(f'm3u8_url:{m3u8_url}')
                m3u8_url = url_m3u8.replace(url_m3u8.split('/')[-1], m3u8_url)
                # print(f'm3u8_url:{m3u8_url}')     # 此时的m3u8地址，就是带有ts的地址
                # get_ts_url(url=m3u8_url, path=path, videoName=videoName)
                getVideo_requests(url=m3u8_url, path=path, videoName=videoName)

    print(f'Download OK!')
