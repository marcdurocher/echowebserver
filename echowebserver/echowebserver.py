"""
EchoWebServer : A HTTP server that echoes POST body requests

__author__ = Marc Durocher

"""
import tornado.ioloop
import tornado.web
import logging


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("GET : OK\n")

    def post(self):
        self.write("POST:  OK\n")
        logger.info(str(self.request.body))
 

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    logger = logging.getLogger('echowebserver')
    logger.setLevel(logging.INFO)
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

