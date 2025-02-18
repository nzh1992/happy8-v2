# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/15
Last Modified: 2025/2/15
Description: 
"""
from werkzeug.security import generate_password_hash, check_password_hash

from app.extentions import db
from app.utils.log import logger
from app.exceptions.system import DatabaseException


class User(db.Model):
    """用户表"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def create_user(self, account, password):
        try:
            password_hash = generate_password_hash(password)
            new_user = User(account=account, password_hash=password_hash)
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            error_info = f"创建用户失败，错误信息：{e}"
            logger.error(error_info)
            raise DatabaseException(error_info)
        else:
            logger.info(f"创建用户成功, account:{account}")

    def login_user(self, account, password):
        try:
            user = User.query.filter_by(account=account).first()
            if user and check_password_hash(user.password_hash, password):
                return user

            return None
        except Exception as e:
            error_info = f"登录失败，错误信息：{e}"
            logger.error(error_info)
            raise DatabaseException(error_info)
