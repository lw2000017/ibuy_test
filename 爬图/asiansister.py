# -*- coding:utf-8 -*-
# @Time     :2019/06/21  13:39
# @Author   :刘向上
# @File     :asiansister.py
# @Order    :https://www.asiansister.com/


import urllib3
import requests
import re
import os
import time


class asiansister():
    def __init__(self):
        print('run~')
        self.url = 'https://www.asiansister.com/'

        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/71.0.3578.80 Safari/537.36'
        cookie = '__cfduid=dc5599d0d2418adc3902abc3c34e7f33f1561095486; ' \
                 'PHPSESSID=0653fce1e5e53f06f76f5888e340b999; splash_i=false; ' \
                 '_ga=GA1.2.48073101.1561095489; _gid=GA1.2.281844247.1561095489; ' \
                 'HstCfa4130490=1561095490876; HstCmu4130490=1561095490876; HstCnv4130490=1; ' \
                 '__dtsu=D9E9B66B476D0C5DEA5E636E029AB970; _gat_gtag_UA_110048501_1=1; HstCns4130490=2;' \
                 ' splashWeb-2960372-42=1; HstCla4130490=1561097917957; HstPn4130490=4; HstPt4130490=4'

        self.headers = {
            'user-agent': user_agent,
            'cookie': cookie,
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1'
        }
        self.path = '/Users/pleasecallme/Documents/图片/asiansister/'

    def get_index_page_item(self):
        # 获取第一页所有相册的链接
        urllib3.disable_warnings()
        res = requests.get(self.url, self.headers, verify=False).text
        item = re.findall('<a href=\'(.*?)\' style="text-decoration: none;">.*?<div class="titleName">(.*?)'
                          '</div>.*?</a>', res, re.S)
        # print(item)
        # _page=num
        for i in range(len(item)):
            titleName = item[i][1].strip()
            page_url = item[i][0]
            self.get_page_index(page_url, titleName)
            time.sleep(3)

    def get_page_index(self, page_url, titleName):
        print(f'正在获取 {titleName} 的所有图片')
        urllib3.disable_warnings()
        res = requests.get(self.url + page_url, self.headers, verify=False)
        img_url_all = re.findall("img class='lazyload showMiniImage'.*?data-src='(.*?)' width=.*?/>", res.text, re.S)
        img_url = []
        # 如果使用原有的链接，图片非常小，通过查找发现，url中去掉_t后，图片变为了大图片
        for i in range(len(img_url_all)):
            img_url.append(img_url_all[i].replace('_t.jpg', '.jpg'))    # 去掉小图片限制的详细图片链接
        print(f'{titleName} 所有图片获取完毕！')
        print('---' * 10)
        for n in range(len(img_url)):
            self.download_img(titleName, img_url[n])
            time.sleep(1)

    def download_img(self, titleName, imgurl):
        # 先判断是否存在文件夹
        img_title = imgurl.replace('images/items/', '').split('/')[-1]
        folder_path = self.path + f'{titleName}'
        img_path = self.path + f'{titleName}' + f'/{img_title}'
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        if not os.path.exists(img_path):
            with open(img_path, 'wb') as f:
                r = self.get_img(self.url + imgurl)
                f.write(r.content)
                f.close()
                print(f'{img_title} 保存成功')
                print('---' * 3)
        else:
            print(f'{titleName}--{img_title} 文件已存在')

    def get_img(self, url):
        urllib3.disable_warnings()
        res = requests.get(url, verify=False)
        return res

    def run(self):
        self.get_index_page_item()


if __name__ == '__main__':
    run = asiansister()
    run.run()


