from flask import Flask
from flask_script import Manager

from app.views import blue
from app.models import db

app = Flask(__name__)

app.register_blueprint(blueprint=blue,url_prefix='/app')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask6'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

manage = Manager(app)

if __name__ == '__main__':
    manage.run()