# -*- coding:utf-8 -*-
# @Time     :2019/06/12  09:43
# @Author   :刘向上
# @File     :毒鸡汤.py
# @Order    :http://www.nows.fun/ 毒鸡汤网站，爬去毒鸡汤

import requests
import time
import re


def get_sentence():
    url = 'http://www.nows.fun/'
    headers = {
        'Cookie': 'PHPSESSID=bdbd13630c54346lr9j4la3er1; UM_distinctid=16b46bfa86c534-00cdb7c9177ccf-13396e57-'
                  '1aeaa0-16b46bfa86da6b; CNZZDATA5406879=cnzz_eid%3D1069410606-1560260090-%26ntime%3D1560299396',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.80 Safari/537.36'
    }
    res = requests.get(url, headers=headers).content.decode('utf-8')
    sentence = re.findall('<span id="sentence".*?">(.*?)</span>.*?</div>', res, re.S)
    print(sentence)
    add_sentence(sentence)


def add_sentence(sentence):
    with open('/Users/pleasecallme/Documents/毒鸡汤.txt', 'a+') as f:
        f.write(sentence[0] + '\n')
        f.close()


def run():
    for i in range(100):
        get_sentence()
        time.sleep(3)


def duplicate_removal():
    """去重，去除重复的信息"""
    with open('/Users/pleasecallme/Documents/毒鸡汤.txt', 'r') as f:
        f_all = f.readlines()
        with open('/Users/pleasecallme/Documents/毒鸡汤_去重后.txt', 'a+') as f_write:
            f_w = []
            for i in f_all:
                if i not in f_w:
                    f_w.append(i)

            for n in f_w:
                f_write.writelines(n)
            f_write.close()

        f.close()


if __name__ == '__main__':
    run()   # 开始爬取
    # duplicate_removal()     # 去除重复信息


