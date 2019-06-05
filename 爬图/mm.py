# -*- coding:utf-8 -*-          
# __Time__     :2019/6/3 14:25    
# __Author__   :LW                         


# 在python3下测试
import requests
import threading
import datetime

count = 0


def Handler(start, end, url, filename):
    # headers = {'Range': 'bytes=%d-%d' % (start, end-1)}
    # r = requests.get(url, headers=headers, stream=True)
    for i in filename[start:end]:
        global count
        r = requests.get("https://youku.cdn2-youku.com/20180701/12972_72ec5f94/1000k/hls/" + i.replace("\n", ""),
                         stream=True)
        # r = requests.get(url)
        with open("ts/" + i.replace("\n", ""), "wb") as code:
            code.write(r.content)
        count = count + 1
        print("下载进度：%.2f" % (count / len(filename)))


def download_file(url, num_thread=100):
    f = open('index.m3u8', 'r', encoding='utf-8')
    text_list = f.readlines()
    s_list = []
    for i in text_list:
        if i.find('#EX') == -1:
            s_list.append(i)

    f.close()
    file_size = len(s_list)

    # 启动多线程写文件
    part = file_size // num_thread  # 如果不能整除，最后一块应该多几个字节
    for i in range(num_thread):
        start = part * i
        if i == num_thread - 1:  # 最后一块
            end = file_size
        else:
            end = start + part

        t = threading.Thread(target=Handler, kwargs={'start': start, 'end': end, 'url': url, 'filename': s_list})
        t.setDaemon(True)
        t.start()

    # 等待所有线程下载完成
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    # print('%s 下载完成' % file_name)


if __name__ == '__main__':
    url = "https://youku.cdn2-youku.com/20180701/12972_72ec5f94/1000k/hls/"
    start = datetime.datetime.now().replace(microsecond=0)
    download_file(url)
    end = datetime.datetime.now().replace(microsecond=0)
    print("用时: ", end='')
    print(end - start)




