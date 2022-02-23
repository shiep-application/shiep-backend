from werkzeug.exceptions import HTTPException
import json
from flask import jsonify


class APIException(HTTPException):
    code = 400
    message = 'Sorry, there was an unexpected error(*^v^*)'

    def __init__(self, msg=None, code=None, headers="application/json"):

        self.headers = headers
        if code:
            self.code = code
        if msg:
            self.message = msg
        super().__init__(msg, None)

    def get_body(self, environ=None):  # 这里是将数据改成指定的json格式
        body = dict(
            error_code=self.error_code,
            msg=self.message
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):  # 这里主要是想指定格式  application/json
        return [("Content-Type", self.headers)]

class UNKNOWN_EXCEPTION(APIException):
    code = 00000
    message = "发生了未知的错误"
class WX_OPENID_FAILED(APIException):
    code = 10001
    message = "微信开放平台后台错误"

class USER_NOT_BOUND(APIException):
    code = 20001
    message = "未绑定用户，请先绑定"
class USER_ALREADY_BOUND(APIException):
    code = 20002
    message = "请勿重复绑定"

err_list = {
    WX_OPENID_FAILED,
    USER_NOT_BOUND, USER_ALREADY_BOUND,
}


def custom_exception_handlers(app):
    for cls in err_list:
        @app.errorhandler(cls)
        def _(exc):
            return jsonify({"code": exc.code, "message": exc.message})