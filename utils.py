import time
import json

from tornado.web import RequestHandler

from constants import API_STATUS_CODE, API_CODE_MESSAGE_MAP
from databases import session
from settings import logger
from tools import extract_log_param


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

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.request_method = "{0} {1}".format(self.request.method, self.request.uri)
        self.response_method = "{0}.{1}".format(self.__module__, self.__class__.__name__)
        self.start_time = time.time()

    def initialize(self):
        self.set_header("Access-Control-Allow-Origin", "*")

        # parameter log
        log_base_formatter = "Parameter: " \
                             "[request_method={0}] [response_method={1}] " \
                             "[remote_ip={2}] [user_agent={3}]"
        log_base = log_base_formatter.format(
            self.request_method,
            self.response_method,
            self.request.remote_ip,
            self.request.headers["User-Agent"]
        )
        logger.info("{0} {1}".format(log_base, extract_log_param(self.request.arguments)))

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
        log_base = "Exit: [request_method={0}] [response_method={1}] [time_cost={2:f}s]"
        logger.info(log_base.format(self.request_method, self.response_method, duration))

    def data_received(self, chunk):
        pass

