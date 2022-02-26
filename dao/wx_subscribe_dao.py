from db.db_singleton_provider import db
from db.db_model import *
import json


def check_subscriber_wx(username):
    results = db.session.query(SubscribeUserWX).filter_by(username=username).all()
    # 未绑定用户
    if len(results) == 0:
        return False
    # 已绑定用户
    else:
        return True


def add_a_subscriber_wx(username, password):
    try:
        subscriber = SubscribeUserWX(username=username, sub_times=0)
        db.session.add(subscriber)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def remove_a_subscriber_wx(username, password):
    try:
        SubscribeUserWX.query.filter(SubscribeUserWX.username == username).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def add_subscribe_times_wx(username):
    try:
        sub_user = db.session.query(SubscribeUserWX).filter_by(username=username).all()[0]
        sub_times = sub_user.sub_times + 1
        SubscribeUserWX.query.filter(SubscribeUserWX.username == username).update({'sub_times': sub_times})

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def subtract_subscribe_times_wx(username):
    try:
        sub_user = db.session.query(SubscribeUserWX).filter_by(username=username)
        print(sub_user)
        sub_times = sub_user.sub_times - 1
        SubscribeUserWX.query.filter(User.username == username).update({'sub_times': sub_times})

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def query_subscriber_wx(username):
    results = db.session.query(SubscribeUserWX).filter_by(username=username).all()
    return results[0]
