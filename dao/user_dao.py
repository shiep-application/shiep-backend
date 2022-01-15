from db.db_singleton_provider import app
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import re
from config import *
import json
from flask import request


@app.route('/job_start', methods=["GET"])
def job_start():
    sched = BackgroundScheduler(timezone='Asia/Shanghai')

    job = sched.add_job(xxx, 'interval', seconds=30, id="grade_query", max_instances=10)
    sched.start()

    return "done"


@app.route('/job_pause', methods=["GET"])
def job_pause():
    job_name = request.args.get("job_name")
    jobs = global_variable.get_value('jobs')
    if job_name not in jobs:
        return "no such job:("

    job = jobs[job_name]["instance"]
    try:
        job.pause()
    except Exception as e:
        return "we might face some problem:("

    return "done"


@app.route('/job_resume', methods=["GET"])
def job_resume():
    job_name = request.args.get("job_name")
    jobs = global_variable.get_value('jobs')
    if job_name not in jobs:
        return "no such job:("

    job = jobs[job_name]["instance"]
    try:
        job.resume()
    except Exception as e:
        return "we might face some problem:("

    return "done"


@app.route('/job_status', methods=["GET"])
def job_status():
    job_name = request.args.get("job_name")
    jobs = global_variable.get_value('jobs')
    if job_name not in jobs:
        return "no such job:("

    job = jobs[job_name]["instance"]
    jobs = global_variable.get_value("jobs")
    status= jobs[job_name]["status"]
    if status == 'down':
        return "maybe down:("
    if re.search('pause+', str(job)):
        # spider_once(trigger: interval[0:00:10], paused)
        return "pause"
    elif re.search('run+', str(job)):
        # spider_once(trigger: interval[0:00:10], next run at: 2021-12-12 19:36:32 CST)
        return "active"
    else:
        return "maybe down:("