from settings import logger
from utils import APIBaseHandler
from databases import session
from .db import AP
from tools import extract_obj_attr


class MainHandler(APIBaseHandler):
    def get(self):
        self.write("Hello, world")


class APInfoPersistenceHandler(APIBaseHandler):

    def post(self):
        ap = AP(online=0)
        return None

    def get(self):
        mac = "10:0D:0E:20:8C:28"
        q = session.query(AP)
        q = q.filter_by(mac=mac).first()
        q = extract_obj_attr(q)
        logger.debug(q)
        return self.json_response(status_code=200, result=q)
