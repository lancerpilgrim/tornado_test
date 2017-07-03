from utils import APIBaseHandler


class MainHandler(APIBaseHandler):
    def get(self):
        self.write("Hello, world")


class APInfoPersistenceHandler(APIBaseHandler):

    def post(self):
        return None

    def get(self):
        return self.json_response(status_code=200)
