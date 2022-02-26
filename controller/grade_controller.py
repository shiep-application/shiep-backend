from db.db_singleton_provider import app
from service.code2userinfo import *
from dao.wx_subscribe_dao import *
from flask import request


@app.route('/api/grade_query_once', methods=["POST"])
def grade_query_once():

    username = request.json.get("username")
    password = request.json.get("password")
    code = request.json.get("code")

    # 来自网页端的请求可以直接处理
    if code is None:
        if username is None or password is None:
            raise PARAM_IS_NULL
        username = username.strip()
        password = password.strip()
        res = grade_query_from_remote(username, password)
    # 来自微信小程序的请求需先处理code
    else:
        code = code.strip()
        user = code2userinfo(code)
        username = str(user.username).strip()
        password = str(user.password).strip()
        res = grade_query_from_remote(username, password)

    return res

