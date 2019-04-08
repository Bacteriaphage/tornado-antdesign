import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('./view/index.html')

if __name__=='__main__':
    app = tornado.web.Application(
            handlers = [(r'/', IndexHandler),],
            static_path = os.path.join(os.path.dirname(__file__), "static")
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
