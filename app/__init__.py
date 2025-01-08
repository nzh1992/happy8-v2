import os

from flask import Flask

from .data import HistoryData
from .extensions import db
from .utils.log import logger


def create_app():
    app = Flask(__name__)

    config_app(app)

    init_extensions(app)

    register_blueprints(app)

    # init database
    with (app.app_context()):
        from .models.reds import RedsModel
        from .models.prize import (PrizeX10Model, PrizeX9Model, PrizeX8Model, PrizeX7Model, PrizeX6Model, \
            PrizeX5Model, PrizeX4Model, PrizeX3Model, PrizeX2Model, PrizeX1Model)
        from .models.statistic import ValueStatisticModel

        db.create_all()
        logger.info("初始化数据库，成功。")

    create_log_dir(app)

    return app


def config_app(app):
    # base setting
    app.config['SECRET_KEY'] = 'secretwfejkasjdglk;jqwlkgnasjdflkad;ng'

    # flask-sqlalchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/happy8'


def init_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    from .apis.index import index_bp
    from .apis.reds import reds_bp
    from .apis.prize import prize_bp
    from .apis.statistic import statistic_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(reds_bp)
    app.register_blueprint(prize_bp)
    app.register_blueprint(statistic_bp)


def create_log_dir(app):
    # 创建日志目录
    log_dir = os.path.join(os.path.dirname(app.root_path), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)
        app.log_dir = log_dir
        logger.info("创建日志目录，成功。")