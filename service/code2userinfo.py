from manager.grade_manager import *
from flask import request
from api_exception import *
from dao.user_dao import *


def check_and_login(code):
    url = "https://api.weixin.qq.com/sns/jscode2session?" \
          "appid=wxf7b1dedbb710515a&" \
          "secret=6f83949ea64601e64f3e3d48deba3ece&" \
          "js_code=" + code + "&" +\
          "grant_type=authorization_code"

    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        res = json.loads(response.text)
        if "errcode" not in res:
            session_key = res["session_key"]
            openid = res["openid"]
            # return {"session_key": session_key, "openid": openid}
            # 去数据库查找用户的学号信息
            if check_user_bound(session_key, openid):
                return "success"
            # 如果是第一次登录，引导用户绑定
            else:
                raise USER_NOT_BOUND
        else:
            raise WX_OPENID_FAILED
    else:
        raise WX_OPENID_FAILED


def code2userinfo(code):
    url = "https://api.weixin.qq.com/sns/jscode2session?" \
          "appid=wxf7b1dedbb710515a&" \
          "secret=6f83949ea64601e64f3e3d48deba3ece&" \
          "js_code=" + code + "&" +\
          "grant_type=authorization_code"

    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        res = json.loads(response.text)
        if "errcode" not in res:
            session_key = res["session_key"]
            openid = res["openid"]
            return {"session_key": session_key, "open_id": openid}
        else:
            raise WX_OPENID_FAILED
    else:
        raise WX_OPENID_FAILED