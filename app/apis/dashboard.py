# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description: 
"""
from flask import Blueprint, render_template


dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
def get_dashboard():
    """
    仪表盘页（首页）
    """
    return render_template('index.html')
