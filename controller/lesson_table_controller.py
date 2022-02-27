from db.db_singleton_provider import app
from service.code2userinfo import *
from manager.lesson_table_manager import *
from flask import request
from api_exception import *


@app.route('/api/lesson_table_query', methods=["POST"])
def lesson_table_query():

    username = request.json.get("username")
    password = request.json.get("password")
    code = request.json.get("code")
    termcode = request.json.get("termcode")

    # 来自网页端的请求可以直接处理
    if code is None:
        if username is None or password is None:
            raise PARAM_IS_NULL
        username = username.strip()
        password = password.strip()
        try:
            res = kb_query_from_remote(username, password, termcode)
        except REMOTE_SERVER_PAUSE:
            raise REMOTE_SERVER_PAUSE
        except Exception:
            raise UNKNOWN_EXCEPTION
        return json.dumps(res)
    # 来自微信小程序的请求需先处理code
    else:
        code = code.strip()
        user = code2userinfo(code)
        username = str(user.username).strip()
        password = str(user.password).strip()
        try:
            res = kb_query_from_remote(username, password, termcode)
        except REMOTE_SERVER_PAUSE:
            raise REMOTE_SERVER_PAUSE
        except Exception:
            raise UNKNOWN_EXCEPTION
        return json.dumps(res)
