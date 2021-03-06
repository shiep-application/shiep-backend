import pymysql
from db.db_singleton_provider import db
pymysql.install_as_MySQLdb()


class User(db.Model):
    # 定义表名
    __tablename__ = 'user'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64))
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    sessionkey = db.Column(db.String(128))
    openid = db.Column(db.String(128))


class SubscribeUserWeb(db.Model):
    # 定义表名
    __tablename__ = 'subscribe_user_web'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    grades_length = db.Column(db.Integer)
    lesson_grade_ids = db.Column(db.JSON)


class SubscribeUserWX(db.Model):
    # 定义表名
    __tablename__ = 'subscribe_user_wx'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64))
    sub_times = db.Column(db.Integer)
    lesson_grade_ids = db.Column(db.JSON)


if __name__ == '__main__':

    # 删除所有表
    db.drop_all()

    # 创建所有表
    db.create_all()
#
#     # # 插入数据
#     # test1 = Topic(topic="测试", date="2021-12-10 10:59")
#     # db.session.add(test1)
#     # db.session.commit()