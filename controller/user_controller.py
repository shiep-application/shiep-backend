from db.db_singleton_provider import app
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from manager.grade_manager import *
import re
from config import *
import json
from flask import request
from service.code2userinfo import *
import hashlib
from api_exception import *
from dao.user_dao import *


@app.route('/api/wx_auto_login', methods=["POST"])
def wx_auto_login():
    code = request.json.get("code").strip()
    return check_and_login(code)

@app.route('/api/code2openid', methods=["POST"])
def code2openid():
    code = request.json.get("code").strip()
    return code2userinfo(code)


@app.route('/api/bound_user', methods=["POST"])
def bound_user():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    session_key = request.json.get("session_key").strip()
    open_id = request.json.get("open_id").strip()

    # 验证是否已经是已绑定用户
    if check_user_bound(session_key, open_id):
        raise USER_ALREADY_BOUND

    # 验证账户密码是否正确
    url = "http://api.shiep.xuyuyan.cn:7788/grade_query"
    data = {"username": username, "password": password}
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    response = requests.post(url, json=data, headers=headers)
    res = json.loads(response.text)
    # 身份验证存在错误
    if "code" in res:
        return res
    else:
    # 身份验证通过，添加绑定用户至数据表
        add_user(username, password, session_key, open_id)
        return {"status": "success"}
