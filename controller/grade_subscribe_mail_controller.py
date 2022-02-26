from db.db_singleton_provider import app
from service.code2userinfo import *
from dao.wx_subscribe_dao import *
from flask import request


@app.route('/api/grade_query_subscribe_mail', methods=["POST"])
def grade_query_subscribe_mail():

    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    email = request.json.get("email").strip()

    res = grade_subscribe_start_mail(username, password, email)

    return "done"
