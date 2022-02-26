from db.db_singleton_provider import app
from apscheduler.schedulers.background import BackgroundScheduler
from config import *
import controller.grade_controller
import controller.grade_subscribe_wx_controller
import controller.grade_subscribe_mail_controller
import controller.user_controller
import controller.job_controller
import controller.wxcheck_controller
import global_variable
from api_exception import *


custom_exception_handlers(app)


@app.route('/')
def index():
    return 'Hello Word'


if __name__ == '__main__':
    global_variable._init()
    app.run(
        host=host,
        port=port
    )