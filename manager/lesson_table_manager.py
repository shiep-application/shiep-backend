from api_exception import *
import json
from service.grade_query_subscribe import *
from dao.web_subscribe_dao import *
from api_exception import *


def kb_query_from_remote(username, password, termcode):
    url = "http://api.shiep.xuyuyan.cn:7788/kb_query"
    data = {"username": username, "password": password, "termcode": termcode}
    print(data)
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    response = requests.post(url, json=data, headers=headers)
    res = json.loads(response.text)
    print(res)
    if response.status_code != 200:
        raise REMOTE_SERVER_PAUSE
    if "code" in res:
        return res
    return res

