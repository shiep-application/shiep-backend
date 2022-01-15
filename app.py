from db.db_singleton_provider import app
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import re
from config import *
import json
from flask import request
import controller.grade_controller
import controller.user_controller
import gensim


@app.route('/')
def index():

    return 'Hello Word'


if __name__ == '__main__':
    app.run(
        host=host,
        port=port
    )