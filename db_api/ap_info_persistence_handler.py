from tornado.escape import json_decode

from settings import logger
from databases import session
from utils import APIBaseHandler
from tools import extract_obj_attr
from .models import AP


class MainHandler(APIBaseHandler):
    def get(self):
        self.write("Hello, world")


class APInfoPersistenceHandler(APIBaseHandler):

    def post(self):
        data = json_decode(self.request.body)
        logger.info(data)
        return self.json_response(status_code=200)

    def get(self):
        mac = "10:0D:0E:20:8C:28"
        q = session.query(AP)
        q = q.filter_by(mac=mac).first()
        q = extract_obj_attr(q)
        logger.debug(q)
        return self.json_response(status_code=200, result=q)
