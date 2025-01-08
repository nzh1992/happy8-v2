# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/1/4
Last Modified: 2025/1/4
Description: 
"""
from flask import Blueprint, request

from app.data import HistoryData
from app.extensions import db
from app.utils.response import make_response
from app.utils.transfer import wrap_to_model
from app.models.reds import RedsModel
from app.models.prize import PrizeX10Model
from app.utils.log import logger


statistic_bp = Blueprint('statistic', __name__, url_prefix='/statistic')


@statistic_bp.route('/value', methods=['post'])
def update_value():
    """
    更新和值表

    :return:
    """
    data = request.get_json(force=True)

    from app.models.statistic import ValueStatisticModel

    # 数据库中的期数0
    current_count = ValueStatisticModel.query.count()

    hd = HistoryData()
    # 总共的期数
    total_count = hd.get_history_count()

    update_count = total_count - current_count
    if update_count <= 0:
        return make_response(200, '已是最新，无需更新'), 200

    his_df = hd.get_reds_df(update_count)

    sum_model_list = []

    # 写入数据库
    for row in his_df.iterrows():
        code = row[0]
        red_numbers = [item for item in row[1]]

        # 1. 和值
        red_sum = sum(red_numbers)

        # 2. 平均值
        red_ave = red_sum / len(red_numbers)

        # 3. 奇数个数
        odd_reds = [r for r in red_numbers if r % 2 == 1]
        odd_count = len(odd_reds)

        # 4. 偶数个数
        even_reds = [r for r in red_numbers if r % 2 == 0]
        even_count = len(even_reds)

        sum_model = ValueStatisticModel(code, red_sum, red_ave, odd_count, even_count)
        sum_model_list.append(sum_model)
        logger.info(f"第{code}期sum表更新，成功")

    db.session.add_all(sum_model_list)
    db.session.commit()
    logger.info(f"全部更新完成，共{update_count}期")
    return make_response(200, 'ok'), 200