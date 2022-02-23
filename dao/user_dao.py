from db.db_singleton_provider import db
from db.db_model import *


def check_user_bound(session_key, open_id):
    results = db.session.query(User).filter_by(openid=open_id).all()
    print(results)
    # 未绑定用户
    if len(results) == 0:
        return False
    # 已绑定用户
    else:
        return True


def check_user_bound_and_info(username, password, open_id):
    results = db.session.query(User).filter_by(username=username, password=password, openid=open_id).all()
    print(results)
    # 未绑定用户
    if len(results) == 0:
        return False
    # 已绑定用户
    else:
        return True


def query_user(session_key, open_id):
    results = db.session.query(User).filter_by(openid=open_id).all()
    return results[0]


def add_user(username, password, session_key, open_id):
    try:
        subscriber = User(username=username, password=password, sessionkey=session_key, openid=open_id)
        db.session.add(subscriber)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def alt_user(username, password, open_id):
    try:
        User.query.filter(User.username == username, User.password == password, User.openid == open_id)\
            .update({'username': username, "password": password, "openid": open_id})
        # 提交会话
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
