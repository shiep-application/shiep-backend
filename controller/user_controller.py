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
    return code2open_id(code)


@app.route('/api/check_bound', methods=["POST"])
def check_bound():
    code = request.json.get("code").strip()
    try:
        user_info = code2open_id(code)
    except WX_OPENID_FAILED:
        raise WX_OPENID_FAILED
    except Exception:
        raise UNKNOWN_EXCEPTION
    print(user_info)
    session_key = user_info["session_key"]
    open_id = user_info["open_id"]
    if check_user_bound(session_key, open_id):
        return "true"
    else:
        return "false"


@app.route('/api/bound_user', methods=["POST"])
def bound_user():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    session_key = request.json.get("session_key").strip()
    open_id = request.json.get("open_id").strip()

    return check_and_bound(username, password, open_id, session_key)


@app.route('/api/cancel_bound_user', methods=["POST"])
def cancel_bound_user():
    code = request.json.get("code").strip()

    try:
        user = code2userinfo(code)
    except WX_OPENID_FAILED:
        raise WX_OPENID_FAILED

    session_key = user.sessionkey
    open_id = user.openid
    username = str(user.username).strip()
    password = str(user.password).strip()

    try:
        return check_and_cancel(username, password, open_id, session_key)
    except REMOTE_SERVER_PAUSE:
        raise REMOTE_SERVER_PAUSE




