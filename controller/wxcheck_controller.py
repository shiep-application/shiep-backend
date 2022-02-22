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
    tmpStr = hashlib.sha1(tmpStr).hexdigest()

    print("tmpStr: " + str(tmpStr))
    print("signature: " + str(signature))
    if tmpStr == signature:
        print("equal")
        return echostr
    else:
        print("not equal")
        return ""


@app.route('/api/wx_post_code', methods=["POST"])
def wx_post_code():
    code = request.json.get("code").strip()
    url = "https://api.weixin.qq.com/sns/jscode2session?" \
          "appid=wxf7b1dedbb710515a&" \
          "secret=6f83949ea64601e64f3e3d48deba3ece&" \
          "js_code=" + code + "&" +\
          "grant_type=authorization_code"

    response = requests.get(url)
    print(response.status_code)
    print(response.text)
    res = json.loads(response.text)
    session_key = res["session_key"]
    openid = res["openid"]
    return ""
