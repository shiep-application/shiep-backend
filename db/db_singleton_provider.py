from flask import Flask
from config import *
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


class Config(object):
    # 设置连接数据库的URL
    user = user
    password = password
    database = database
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

    # 设置sqlalchemy自动更跟踪数据库
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = SQLALCHEMY_ECHO
    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = SQLALCHEMY_COMMIT_ON_TEARDOWN


app.config.from_object(Config)
# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)