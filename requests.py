from tornado.web import RequestHandler

class HelloRequest(RequestHandler):
    def get(self):
        self.write("Hello world!")

