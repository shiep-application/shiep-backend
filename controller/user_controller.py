from db.db_singleton_provider import app
from manager.user_manager import *
from service.check_username_and_password import *
from dao.user_dao import *


@app.route('/api/wx_auto_login', methods=["POST"])
def wx_auto_login():
    code = request.json.get("code").strip()
    return check_and_login(code)


@app.route('/api/code2openid', methods=["POST"])
def code2openid():
    code = request.json.get("code").strip()
    return code2userinfo(code)


@app.route('/api/check_bound', methods=["POST"])
def check_bound():
    code = request.json.get("code").strip()
    user_info = code2userinfo(code)
    session_key = user_info["session_key"]
    open_id = user_info["openid"]
    if check_user_bound(session_key, open_id):
        return True
    else:
        return False


@app.route('/api/bound_user', methods=["POST"])
def bound_user():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    session_key = request.json.get("session_key").strip()
    open_id = request.json.get("open_id").strip()

    return check_and_bound(username, password, open_id, session_key)

