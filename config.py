# 数据库配置 ###########################################################################
user = 'root'
password = 'wykbjdy999'
database = 'shiep_application'
ip = '119.45.236.94'
# ip = '127.0.0.1'
database_uri = 'mysql://%s:%s@%s:3306/%s?charset=utf8mb4' % (user, password, ip, database)
# 设置sqlalchemy自动更跟踪数据库
SQLALCHEMY_TRACK_MODIFICATIONS = True
# 查询时会显示原始SQL语句
SQLALCHEMY_ECHO = True
# 禁止自动提交数据处理
SQLALCHEMY_COMMIT_ON_TEARDOWN = False

# app_config #########################################################################
host = '127.0.0.1'
port = 6677