# -*- coding:utf-8 -*-          
# @Time     :2019/5/2 16:53    
# @Author   :LW                 
# @File     :m3u8.py         


import requests
import time
import xlwt
import re
from bs4 import BeautifulSoup
import xlrd


# 第一次搜索，查看搜索页的全部内容
def Search(guanjianzi):
    now = int(time.time())
    search_url = ''
    cookie = '__cfduid=d48935a19fa9c9a6fb304c90b7fc9bde41556786231; PHPSESSID=4u5olhtrust6p6hn5r18pv5dg0;' \
             ' Hm_lvt_f6a8bb3e30850d0127c484619f0210c7=1556786235; ' \
             'Hm_lpvt_f6a8bb3e30850d0127c484619f0210c7={}'.format(now)
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/64.0.3282.204 Safari/537.36'
    headers = {
        'Cookie': cookie,
        'User-Agent': User_Agent,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    form = {
        'wd': guanjianzi,
        'cid': ''
    }
    response = requests.post(url=search_url, headers=headers, data=form)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


# 获取详情页的链接以及标题
def detail(soup):
    channel = soup.find_all('a', attrs={'class': 'videoName'})
    # print(channel)
    detail_url = []
    detail_name = []
    for i in channel:
        a = i.get('href')      # 详情页的链接
        b = i.get('title')    # 可以当做是标题
        detail_url.append(a)
        detail_name.append(b)
    return detail_name, detail_url


# 判断是否有下一页，若有，则继续请求
def judge_net_page(soup):
    # soup = BeautifulSoup(response.text, 'html.parser')
    channel = soup.find_all('a', attrs={'target': '_self'})
    for i in channel:
        if i.get_text() == '下一页':
            next_page = i.get('href')
            return next_page


# 再次请求，请求的是下一页的内容
def again(url):
    now = int(time.time())
    cookie = '__cfduid=d48935a19fa9c9a6fb304c90b7fc9bde41556786231; PHPSESSID=4u5olhtrust6p6hn5r18pv5dg0; ' \
             'Hm_lvt_f6a8bb3e30850d0127c484619f0210c7=1556786235; ' \
             'Hm_lpvt_f6a8bb3e30850d0127c484619f0210c7={}'.format(now)
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/64.0.3282.204 Safari/537.36'
    headers = {
        'Cookie': cookie,
        'User-Agent': User_Agent,
        # 'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


# 获取详情页的m3u8地址
def index(url):
    now = int(time.time())
    cookie = '__cfduid=d48935a19fa9c9a6fb304c90b7fc9bde41556786231; PHPSESSID=4u5olhtrust6p6hn5r18pv5dg0; ' \
             'Hm_lvt_f6a8bb3e30850d0127c484619f0210c7=1556786235; ' \
             'Hm_lpvt_f6a8bb3e30850d0127c484619f0210c7={}'.format(now)
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/64.0.3282.204 Safari/537.36'
    headers = {
        'Cookie': cookie,
        'User-Agent': User_Agent,
        # 'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.get(url=url, headers=headers)
    m3u8_url_xx = re.findall('<a href=".*" title=".*" target="_blank">(.*?)</a>', response.text, re.S)
    for i in range(len(m3u8_url_xx)):
        m3u8_url = m3u8_url_xx[i][4:]
        print(m3u8_url)
    return m3u8_url


# 写入工作表
def write_work_book(detail_name, detail_url, path, sheet):
    workbook = xlwt.Workbook()  # 创建一个excel
    sheet = workbook.add_sheet(f"{sheet}")     # 创建sheet名
    row0 = ['标题', '链接']
    # 先创建第一行的标题
    for j in range(len(row0)):
        sheet.write(0, j, row0[j])
    # 再把获取到的数据，逐行添加进去
    for i in range(len(detail_name)):
        rows = [detail_name[i], detail_url[i]]
        sheet.write(i+1, 0, rows[0])
        sheet.write(i+1, 1, rows[1])
    # 保存excel
    workbook.save(path)


if __name__ == '__main__':
    # 关键字，可修改
    guanjianzi = '网红'
    sheet = 'Sheet1'
    # 文件名
    path = '{}.xls'.format(guanjianzi)
    # 配置文件位置
    session = 'C:\\Users\please call me\Pictures\表情管理\M3U8 1.4.2\\aria2.session'
    # url = 'http://www.605daohang.com/'
    # # 搜索接口，输入关键字即可搜素
    # search_url = 'http://www.605daohang.com/index.php?m=vod-search'
    # soup = Search(guanjianzi)
    # detail_name = []
    # detail_url = []
    # m3u8_url = []
    # # 判断是否有下一页
    # next_page = judge_net_page(soup=soup)
    # # 判断是否有下一页，若有，则继续访问下一页的内容，若无，则只访问当前页的内容
    # while next_page is not None:
    #     soup1 = again(url=url + next_page)
    #     detail_name_xx = detail(soup=soup1)[0]
    #     detail_url_xx = detail(soup=soup1)[1]
    #     for i in range(len(detail_name_xx)):
    #         detail_name.append(detail_name_xx[i])
    #         detail_url.append(detail_url_xx[i])
    #     for i in range(len(detail_url_xx)):
    #         m3u8_url.append(index(url=url + detail_url_xx[i]))
    #
    #     next_page = judge_net_page(soup=soup1)
    # else:
    #     detail_name_xx = detail(soup=soup)[0]
    #     detail_url_xx = detail(soup=soup)[1]
    #     for i in range(len(detail_name_xx)):
    #         detail_name.append(detail_name_xx[i])
    #         detail_url.append(detail_url_xx[i])
    #     for i in range(len(detail_url_xx)):
    #         m3u8_url.append(index(url=url + detail_url_xx[i]))
    #
    # print("获取完毕")
    # # 写入工作簿
    # write_work_book(detail_name, m3u8_url, path, sheet=sheet)

    workbook = f'{guanjianzi}.xls'
    data = xlrd.open_workbook(workbook)
    table = data.sheet_by_name(f'{sheet}')
    rows = table.nrows  # 获取总行数
    for i in range(1, rows):
        # 从第二行开始获取（第一行是标题）
        videoName = table.row_values(i)[0]  # 文件标题
        url_m3u8 = table.row_values(i)[1]  # m3u8地址
        videoName = videoName.replace(',', ' ')
        videoName = videoName.replace('，', ' ')
        # print(videoName)
        with open(session, 'a+', encoding='utf-8', errors='ignore') as f:
            f.write(f'{videoName},{url_m3u8}\n')
            f.close()
