from db.db_singleton_provider import db
from db.db_model import *


def check_user_bound(session_key, open_id):
    results = db.session.query(User).filter_by(sessionkey=session_key, openid=open_id).all()
    print(results)
    # 是未绑定用户
    if len(results) == 0:
        return False
    else:
        return True


def query_user(session_key, open_id):
    results = db.session.query(User).filter_by(sessionkey=session_key, openid=open_id).all()
    return results[0]


def add_user(username, password, session_key, open_id):
    try:
        subscriber = User(username=username, password=password, sessionkey=session_key, openid=open_id)
        db.session.add(subscriber)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e