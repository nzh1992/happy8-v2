# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/3
Last Modified: 2025/2/3
Description: 
"""
from flask import Blueprint, render_template, request, redirect, url_for

from app.models.user import User
from app.utils.log import logger
from app.utils.response import make_response


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录
    """
    if request.method == 'GET':
        return render_template('login.html')

    try:
        account = request.form.get("account")
        password = request.form.get("password")
        result = User().login_user(account, password)
    except Exception as e:
        raise e
    else:
        logger.info(f"登录成功. account: {account}")
        return redirect(url_for('dashboard.get_dashboard'))


@user_bp.route('/', methods=['POST'])
def create_user():
    """
    创建用户
    """
    try:
        data = request.get_json(force=True)
        account = data.get("account")
        password = data.get("password")

        User().create_user(account, password)
    except Exception as e:
        raise e
    else:
        return make_response(0, "ok"), 200
