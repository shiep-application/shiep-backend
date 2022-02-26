from db.db_singleton_provider import app
from service.code2userinfo import *
from dao.wx_subscribe_dao import *
from flask import request


@app.route('/api/grade_subscribe_or_add_times_wx', methods=["POST"])
def grade_subscribe_or_add_times():

    code = request.json.get("code").strip()
    # 通过code获取用户信息
    user = code2userinfo(code)
    username = str(user.username).strip()
    password = str(user.password).strip()
    # 如果用户已经在订阅表，则增加订阅次数
    if check_subscriber_wx(username):
        add_subscribe_times_wx(username)
    # 如果用户不在则新增订阅用户
    else:
        add_a_subscriber_wx(username, password)
    return "done"


@app.route('/api/grade_cancel_subscribe', methods=["POST"])
def grade_cancel_subscribe():

    code = request.json.get("code").strip()
    # 通过code获取用户信息
    user = code2userinfo(code)
    username = str(user.username).strip()
    password = str(user.password).strip()
    # 如果用户已经在订阅表，则增加订阅次数
    if check_subscriber_wx(username):
        remove_a_subscriber_wx(username, password)
    return "success"


@app.route('/api/if_grade_subscribe_wx', methods=["POST"])
def if_grade_subscribe_wx():

    code = request.json.get("code").strip()
    # 通过code获取用户信息
    user = code2userinfo(code)
    username = str(user.username).strip()
    password = str(user.password).strip()

    sub_status = check_subscriber_wx(username)
    sub_times = 0
    print(sub_status)
    if sub_status:
        sub_user = query_subscriber_wx(username)
        sub_times = sub_user.sub_times

    return {"sub_status": sub_status, "sub_times": sub_times}