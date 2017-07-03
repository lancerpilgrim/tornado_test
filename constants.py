class API_STATUS_CODE:
    API_CODE_OK = 200
    API_REQUIRED = 400
    API_BAD_REQUEST = 400
    API_UNAUTHORIZED = 401
    API_FORBIDDEN = 403
    API_NOT_FOUND = 404
    API_SERVICES_UNAVAILABLE = 503


class API_CODE_MESSAGE:
    API_CODE_OK = "OK"
    API_BAD_REQUEST = "请求数据格式错误"
    API_REQUIRED = "参数错误"
    API_UNAUTHORIZED = "用户没有登录"
    API_FORBIDDEN = "用户没有权限"
    API_NOT_FOUND = "请求资源不存在"
    API_SERVICES_UNAVAILABLE = "服务不可用"


API_CODE_MESSAGE_MAP = {
    "200": "OK",
    "400": "请求数据格式错误",
    "401": "用户没有登录",
    "403": "用户没有权限",
    "404": "请求资源不存在",
    "503": "服务不可用"
}


if __name__ == "__main__":
    print(API_CODE_MESSAGE.API_CODE_OK)
