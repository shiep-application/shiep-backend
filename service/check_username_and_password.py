from service.code2userinfo import *
from api_exception import *


def check_username_and_password(username, password):
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
        return "success"
