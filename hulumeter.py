import os
import traceback
import logging

import tornado.web
import tornado.ioloop

import cfg
from requests import *

def get_application(debug=False):
    try:
        settings = {
            'static_path': os.path.join(cfg.root, "static"),
            'debug': True
        }
        application = tornado.web.Application([
            (r'/',HelloRequest),
            (r'/scores/', ScoresRequest),
        ], **settings)

        return application

    except Exception, e:
        logging.error("Error: %s" % traceback.format_exc())
        raise e

application = get_application()

if __name__ == "__main__":
    application = get_application(debug=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
