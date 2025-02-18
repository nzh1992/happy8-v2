# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/18
Last Modified: 2025/2/18
Description: 
"""
import os

from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd

from app.models.happy8_number import Happy8NumberModel
from app.utils.log import logger
from app.utils.response import make_response
from app.utils.file import FileManager


output_bp = Blueprint('output', __name__, url_prefix='/output')


@output_bp.route('/number/<period_count>', methods=['GET'])
def get_number(period_count):
    """
    获取历史开奖号码，生成excel文件
    """
    number_models = Happy8NumberModel.query.order_by(Happy8NumberModel.id.desc()).limit(period_count).all()

    code_list = []
    column_list = [str(i) for i in range(1, 81)]
    period_data_list = []

    for number_model in number_models:
        code_list.append(number_model.code)
        numbers = number_model.get_numbers()

        period_data = [""] * 80
        for number in numbers:
            period_data[number - 1] = str(number)

        period_data_list.append(period_data)

    df = pd.DataFrame(period_data_list, columns=column_list, index=code_list)

    excel_file_name = f"number_{period_count}.xlsx"
    excel_fp = os.path.join(FileManager().get_output_dir(), excel_file_name)
    df.to_excel(excel_fp)

    return "ok"