import requests
import json
from service.grade_query_subscribe import *


def grade_query_from_remote(username, password):
    url = "http://api.shiep.xuyuyan.cn:7788/grade_query"
    data = {"username": username, "password": password}
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    print(response.text)

    grades = []
    xwklist = json.loads(response.text)["xwklist"]
    fxwklist = json.loads(response.text)["fxwklist"]
    for item in xwklist:
        grades.append(item)
    for item in fxwklist:
        grades.append(item)

    return json.dumps(grades)


def grade_subscribe(username, password, email):
    config = read_config()
    grades = json.loads(grade_query_from_remote(username, password))
    length = len(grades)
    sendmail("服务启动成功", generate_html(grades), config, email)
    while True:
        new_grades = json.loads(grade_query_from_remote(username, password))
        if len(new_grades) != length:  # 出新成绩了
            sendmail("出新成绩了！", generate_html(new_grades), config, email)
        time.sleep(60)
