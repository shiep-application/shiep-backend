from db.db_singleton_provider import app
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from manager.grade_manager import *
import re
from config import *
import json
from flask import request


@app.route('/api/grade_query_once', methods=["POST"])
def grade_query_once():

    username = request.json.get("username").strip()
    password = request.json.get("password").strip()

    res = grade_query_from_remote(username, password)

    return res


@app.route('/api/grade_query_subscribe', methods=["POST"])
def grade_query_subscribe():

    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    email = request.json.get("email").strip()

    res = grade_subscribe_start(username, password, email)

    return "done"
