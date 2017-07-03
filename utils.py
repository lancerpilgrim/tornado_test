import time
import json
import tornado
from tornado.web import RequestHandler

from exceptions import ErrCodeUndefinedException
from constants import API_CODE_MESSAGE, API_STATUS_CODE, API_CODE_MESSAGE_MAP
from databases import session
from settings import logger


class JSONResponse(dict):
    def __init__(self, code=API_STATUS_CODE.API_CODE_OK,
                 message=API_STATUS_CODE.API_CODE_OK, **kwargs):

        super().__init__(**kwargs)

        if not kwargs:
            kwargs = {}
        kwargs.update({'code': code, 'message': message})

        self.kwargs = kwargs

    def __str__(self):
        return json.dumps(self.kwargs,
                          cls=JSONResponse.JSONEncoder).replace("</", "<\\/")

    class JSONEncoder(json.JSONEncoder):
        pass


class APIResponse:

    def __init__(self, status_code=None, message=None, *args, **kwargs):
        self.status_code = status_code or API_STATUS_CODE.API_CODE_OK
        self.message = message or API_CODE_MESSAGE_MAP[str(self.status_code)]
        self.response = dict()
        if self.message is not None:
            self.response["message"] = self.message
        self.response["status_code"] = self.status_code
        self.response.update(**kwargs)


class APIException(Exception, APIResponse):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self)
        APIResponse.__init__(self, *args, **kwargs)


class APIBaseHandler(RequestHandler):

    def initialize(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.start_time = time.time()

    def _handle_request_exception(self, e):
        self.set_header("Content-Type", "application/json")
        if isinstance(e, APIException):
            self.set_status(e.status_code)
            self.finish(json.dumps(e.response))
        else:
            session.rollback()
            self.set_status(500)
            self.finish({"code": 500, "reason": str(e)})

    def json_response(self, **kwargs):
        self.set_header("Content-Type", "application/json")
        status_code = kwargs.pop("status_code", None)
        message = kwargs.pop("message", None)
        api_response = APIResponse(
            status_code, message, **kwargs
        )

        self.write(json.dumps(api_response.response))
        self.finish()

    def on_finish(self):
        session.close()
        duration = time.time() - self.start_time
        request_method = "{0} {1}".format(self.request.method, self.request.uri)
        response_method = "{0}.{1}".format(self.__module__, self.__class__.__name__)
        log_base = "Exit: [request_method={0}] [response_method={1}] [time_cost={2:f}s]"
        logger.info(log_base.format(request_method, response_method, duration))


def response_success():
    return JSONResponse()
