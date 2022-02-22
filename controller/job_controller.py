from db.db_singleton_provider import app
from apscheduler.schedulers.background import BackgroundScheduler
import global_variable
from manager.grade_manager import *
import re
from config import *
import json
from flask import request


@app.route('/api/job_start', methods=["GET"])
def job_start():
    sched = BackgroundScheduler(timezone='Asia/Shanghai')
    job = sched.add_job(auto_grade_query_mail, 'interval', seconds=60, id="auto_grade_query", max_instances=10)
    sched.start()

    global_variable.set_value('job', job)
    return "done"


@app.route('/api/job_pause', methods=["GET"])
def job_pause():
    job = global_variable.get_value('job')
    try:
        job.pause()
    except Exception as e:
        return "we might face some problem:("
    return "done"


@app.route('/api/job_resume', methods=["GET"])
def job_resume():
    job = global_variable.get_value('job')
    try:
        job.resume()
    except Exception as e:
        return "we might face some problem:("

    return "done"


@app.route('/api/job_status', methods=["GET"])
def job_status():
    job = global_variable.get_value('job')
    if re.search('pause+', str(job)):
        # spider_once(trigger: interval[0:00:10], paused)
        return "pause"
    elif re.search('run+', str(job)):
        # spider_once(trigger: interval[0:00:10], next run at: 2021-12-12 19:36:32 CST)
        return "active"
    else:
        return "maybe down:("
