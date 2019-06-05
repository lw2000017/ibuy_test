# -*- coding:utf-8 -*-          
# __Time__     :2019/6/5 9:27    
# __Author__   :刘向上
# __Order__    :用来下载狼视频 国产区视频

import requests
import json
import time
import urllib3
import os
import tqdm
import datetime

class ZH_Video():
    def __init__(self):
        self.headers = {
            'Cookie': 'ci_session=Qd%2FnARmDUXQo2jm4NHAv%2B%2BR%2FrjW26756YpjPiN0zM0IdI8DisnPlns2ofOT46V9MRwh2JXB0lFpBTt7SF52%2BUZE%2FXanRULybNpgy9i573f0M6WsHn1%2BF%2B4CafCMbK%2Bf2q2nF73njAtoHvqRLtF6m81V%2FQPKzOjCkCM2gHeKeeb6oAlHm96q3YMwuywYgGHisOugm%2FDteG%2BVHkt6SrMIkO95G%2FBwG0SizQHQKlDoWxS3%2FU3GX%2Fo1X45LT297QvFKesfA1toNiDzhHVSgUIzB9k1GFZ2fSHtKwXNEReCDHcsDZyLVIhie3xmnyUKo%2BdtaTauPbS2koeBftI6W0rxH75AfVQBlFokrecv6XsE%2BaBxi%2Fjjs3hHrhU37aTGLXrein',
            'User-Agent': 'avfun/2.4 (iPhone; iOS 12.0; Scale/2.00)'
        }

    def run(self):
        ZH_Video().get_video_list()


    def get_video_list(self):
        url = 'https://www.5781000.co/api3/get_video_list/cat/102/'
        for i in range(1, 2):
            start = datetime.datetime.now().replace(microsecond=0)
            print(f'正在请求第{i}页数据~~~')
            print('----------'*10)
            urllib3.disable_warnings()      # 屏蔽https警告
            response = requests.post(url=f'{url}{i}', headers=self.headers, verify=False)
            res_json = json.loads(response.content, encoding='utf-8')
            row_list = res_json['rows']
            end = datetime.datetime.now().replace(microsecond=0)
            print(f'第{i}页数据请求完成---{end-start}')
            for n in range(len(row_list)):
                title = row_list[n]['title']    # 标题
                cover = row_list[n]['cover']    # 封面
                up_time = row_list[n]['up_time']    # 更新时间
                category = row_list[n]['category']  # 属性
                cat_text = row_list[n]['cat_text']  # 类别
                startdate = row_list[n]['startdate']    # 创建时间
                id_num = row_list[n]['id']
                sys_ctime = row_list[n]['sys_ctime']    # 时间
                time.sleep(3)
                print(f'正在请求第{i}页第{n}个视频')
                print('-----'*10)
                print(f'{title}创建于{sys_ctime}，更新时间为{up_time}，所在区域为{category}，属于{cat_text}类型')
                self.get_video_data(id_num, title)

    def get_video_data(self, id_num, title):

        start = datetime.datetime.now().replace(microsecond=0)
        url = 'https://www.5781000.co/api3/get_video_data_v2/'
        urllib3.disable_warnings()      # 屏蔽https警告
        response = requests.post(url=f'{url}{id_num}', headers=self.headers, verify=False)
        play_list = json.loads(response.content, encoding='utf-8')['play_list']
        for i in range(len(play_list)):
            video_url = play_list[i].split('.mp4')[0] + '.mp4'
            print(video_url)
            time.sleep(3)
            self.download_video(video_url, path=f'.\\video\\{title}.mp4')


    def download_video(self, video_url, path):
        response = requests.get(video_url, stream=True)
        # print(response.content)
        file_size = int(response.headers['content-length'])
        if os.path.exists(path):
            first_byte = os.path.getsize(path)
        else:
            first_byte = 0
        if first_byte >= file_size:
            return file_size
        headers = {"Range": f"bytes={first_byte}-{file_size}"}
        pbar = tqdm.tqdm(
            total=file_size, initial=first_byte,
            unit='B', unit_scale=True, desc=path)

        req = requests.get(video_url, headers=headers, stream=True)
        with(open(path, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
        pbar.close()
        return file_size


if __name__ == '__main__':
    vi = ZH_Video()
    vi.run()