# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description: 
"""
from flask import Flask

from .utils.log import logger
from .utils.file import FileManager
from .extentions import db


def create_app():
    app = Flask(__name__)

    # 加载配置
    app.config.from_pyfile('config.py')

    # 加载flask扩展
    init_extensions(app)

    # 创建日志目录
    FileManager().create_log_dir()
    # 创建文件输出目录
    FileManager().create_output_dir()

    # 注册路由
    register_blueprints(app)

    # init database
    with ((app.app_context())):
        from .models.happy8_number import Happy8NumberModel
        from .models.happy8_prize import (PrizeX10Model, PrizeX9Model, PrizeX8Model, PrizeX7Model, PrizeX6Model, \
            PrizeX5Model, PrizeX4Model, PrizeX3Model, PrizeX2Model, PrizeX1Model)
        from .models.user import User
        from .models.analyze import ValueModel, NumberCountModel, CurrentMissingModel, HotNumberPeriod10Model, \
            HotNumberPeriod20Model, HotNumberPeriod5Model
        from .models.strategy import CatchMissingX2C5Model

        db.create_all()
        logger.info("初始化数据库，成功。")

    return app


def init_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    from .apis.user import user_bp
    from .apis.dashboard import dashboard_bp
    from .apis.happy8 import happy8_bp
    from .apis.output import output_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(happy8_bp)
    app.register_blueprint(output_bp)
