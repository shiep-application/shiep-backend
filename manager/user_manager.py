from config import *
from service.check_username_and_password import *
from api_exception import *
from dao.user_dao import *


def check_and_bound(username, password, open_id, session_key):
    # 验证是否已经是已绑定用户
    if check_user_bound_and_info(username, password, open_id):
        raise USER_ALREADY_BOUND

    res = check_username_and_password(username, password)
    # 身份验证存在错误
    if res != "success":
        return res
    else:
        # 身份验证通过，添加绑定用户至数据表
        # 如果已经绑定，则修改绑定信息
        if check_user_bound(session_key, open_id):
            alt_user(username, password, open_id)
        # 如果未绑定则新增记录
        else:
            add_user(username, password, session_key, open_id)
        return {"status": "success"}


def check_and_cancel(username, password, open_id, session_key):
    # 验证是否已经是已绑定用户
    if not check_user_bound_and_info(username, password, open_id):
        raise USER_NOT_BOUND

    res = check_username_and_password(username, password)
    # 身份验证存在错误
    if res != "success":
        return res
    else:
        # 身份验证通过，删除绑定信息
        delete_user(username, password, open_id)
        return {"status": "success"}
