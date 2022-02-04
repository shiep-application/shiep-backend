from db.db_singleton_provider import app
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from manager.grade_manager import *
import re
from config import *
import json
from flask import request
import hashlib


@app.route('/api/wxcheck', methods=["GET"])
def wx_check():
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")

    token = "wxcheck"
    tmpArr = [token, timestamp, nonce]

    tmpArr.sort()
    tmpStr = (str(tmpArr[0]) + str(tmpArr[1]) + str(tmpArr[2])).encode('utf-8')
    tmpStr = hashlib.sha1(tmpStr)

    if tmpStr == signature:
        return echostr
    else:
        return ""
