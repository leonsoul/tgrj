# from logging.config import dictConfig
import os
import platform

from flask import Flask
from flask_session import Session

from Demo_utils.logger import Log as log
from app.user_views import user_blueprint

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
if platform.system() == 'Linux':
    static_dir = "/www/wwwroot/tgrj/static"
    templates_dir = "/www/wwwroot/tgrj/templates"
else:
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')
se = Session()


def create_app():
    app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)
    app.register_blueprint(blueprint=user_blueprint)
    app.secret_key = 'KH&c?MXGuS'
    app.config['SESSION_TYPE'] = 'filesystem'
    # app.config['SESSION_TYPE'] = 'sqlalchemy'
    app.config['SECRET_KEY'] = 'KH&c?MXGuS5=D2o8}j@sdP*)'
    app.debug = True
    # db.init_app(app)
    se.init_app(app)
    log.info("启动地址：", static_dir, templates_dir)
    return app
