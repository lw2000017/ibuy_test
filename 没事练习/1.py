# -*- coding:utf-8 -*-          
# @Time     :2019/5/16 21:57    
# @Author   :LW                 
# @File     :1.py         


import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello world!')


def make_app():
    return tornado.web.Application(
        [
            (
                r'/', MainHandler
            ),
        ]
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()