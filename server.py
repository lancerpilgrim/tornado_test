import tornado.ioloop
import tornado.web
from db_api.test import MainHandler, APInfoPersistenceHandler
from settings import logger

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/ap/", APInfoPersistenceHandler)
])


if __name__ == "__main__":
    try:
        logger.info("start")
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        logger.error(e)
