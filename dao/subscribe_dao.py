from db.db_singleton_provider import db
from db.db_model import *


def add_one_subscriber(username, password, email, grades_length):
    try:
        subscriber = SubscribeUserWeb(username=username, password=password, email=email, grades_length=grades_length)
        db.session.add(subscriber)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def check_subscriber_exists(username):
    results = db.session.query(SubscribeUserWeb).filter_by(username=username).all()
    print(results)
    if len(results) == 0:
        print("是新订阅用户")
        return False
    else:
        return True


def get_all_subscribers():
    return SubscribeUserWeb.query.all()


def update_subscriber_grades_len(username, new_len):
    try:
        db.session.query(SubscribeUserWeb).filter(SubscribeUserWeb.username == username).update({SubscribeUserWeb.grades_length: new_len})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
