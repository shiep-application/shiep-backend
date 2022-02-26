from service.grade_query_subscribe import *
from dao.web_subscribe_dao import *
from api_exception import *


def grade_query_from_remote(username, password):
    url = "http://api.shiep.xuyuyan.cn:7788/grade_query"
    data = {"username": username, "password": password}
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    print(response.text)
    if response.status_code != 200:
        raise REMOTE_SERVER_PAUSE
    if "code" in json.loads(response.text):
        return response.text

    grades = []
    xwklist = json.loads(response.text)["xwklist"]
    fxwklist = json.loads(response.text)["fxwklist"]
    for item in xwklist:
        grades.append(item)
    for item in fxwklist:
        grades.append(item)
    grades.sort(key=lambda i: i["cj"], reverse=True)

    return json.dumps(grades)


def check_mail_subscribe(username, password, email, grades_length):
    # 如果订阅用户不在已订阅列表，添加至订阅表
    if not check_subscriber_exists(username):
        add_one_subscriber(username, password, email, grades_length)


def grade_subscribe_start_mail(username, password, email):
    config = read_config()
    grades = json.loads(grade_query_from_remote(username, password))

    length = len(grades)
    check_mail_subscribe(username, password, email, length)

    sendmail("服务启动成功", generate_html(grades), config, email)


def update_grades_len(username, new_len):
    update_subscriber_grades_len(username, new_len)


def auto_grade_query_mail():
    subcribers = get_all_subscribers()
    config = read_config()  # 读取邮件发送配置文件
    for subscriber in subcribers:
        username = subscriber.username
        password = subscriber.password
        email = subscriber.email
        length = subscriber.grades_length

        new_grades = json.loads(grade_query_from_remote(username, password))
        if len(new_grades) != length:  # 出新成绩了
            print("grades_len: " + str(length))
            print("new_grades_len: " + str(len(new_grades)))
            sendmail("出新成绩了！", generate_html(new_grades), config, email)

            # 更新用户成绩长度
            update_grades_len(username, len(new_grades))
