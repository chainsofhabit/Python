import redis
from flask import Flask
from flask_script import Manager
from flask_session import Session
from app.views import blue
from app.models import db
app = Flask(__name__)

app.register_blueprint(blueprint=blue,url_prefix='/app')

#设置加密的复杂程度
app.secret_key = 'qwertyuioplkj'

#配置session存储数据库
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1',
                                          port=6379)


#初始化flask对象app
#第一种
Session(app)

#第二种
# sess = Session()
# sess.init_app(app)

#数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask6'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

#初始化app和db
db.init_app(app)


manage = Manager(app)
if __name__ == '__main__':
    manage.run()