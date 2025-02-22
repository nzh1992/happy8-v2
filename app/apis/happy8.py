# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description: 
"""
import random

from flask import Blueprint

from app.extentions import db
from app.models.happy8_number import Happy8NumberModel
from app.models.happy8_prize import (PrizeX10Model, PrizeX9Model, PrizeX8Model, PrizeX7Model, PrizeX6Model,
                                     PrizeX5Model, PrizeX4Model, PrizeX3Model, PrizeX2Model, PrizeX1Model)
from app.models.analyze import (ValueModel, NumberCountModel, CurrentMissingModel, HotNumberPeriod10Model,
                                HotNumberPeriod20Model, HotNumberPeriod5Model)
from app.models.strategy import CatchMissingX2C5Model
from app.data_source.data import HistoryData
from app.utils.log import logger


happy8_bp = Blueprint('happy8', __name__, url_prefix="/happy8")


@happy8_bp.route('/update', methods=['POST'])
def happy8_update():
    """
    更新开奖号码、奖金情况
    """
    last_model = Happy8NumberModel.get_last_model()

    hd = HistoryData()
    total_count = hd.get_history_count()

    # 待更新期数
    update_count = total_count - last_model.id
    if update_count == 0:
        logger.info("已是最新开奖数据，跳过更新")
        return "ok"

    data = hd.get_data(update_count)

    update_model_list = []
    for info in data.get("result"):
        code = info.get("code")
        reds = [int(i) for i in info.get("red").split(",")]
        update_model = Happy8NumberModel(code, reds)
        update_model_list.append(update_model)

    if update_model_list:
        db.session.add_all(update_model_list)
        db.session.commit()
        logger.info(f"更新开奖数据成功，{len(update_model_list)}期")

    return "ok"


@happy8_bp.route('/init', methods=['POST'])
def happy8_init():
    """
    初始化开奖号码、奖金情况。仅项目初始化时调用一次。
    """
    # Happy8NumberModel.init_data()

    # Happy8NumberModel.init_prize_data()

    # ValueModel.init_value_analyze()

    # NumberCountModel.init_value_count()

    # CurrentMissingModel.init_data()

    # CatchMissingX2C5Model.init_data()

    # HotNumberPeriod10Model.init_data()

    # HotNumberPeriod20Model.init_data()

    HotNumberPeriod5Model.init_data()

    return "dashboard page."


@happy8_bp.route('/hot/<code>', methods=['GET'])
def get_number_count(code):
    """
    获取号码出现累计次数
    """
    d = NumberCountModel.get_hot_numbers(code)

    # 小于377次的
    count_list = [(k, v) for k, v in d.items() if v <= 377]
    count_dict = dict(count_list)

    # 从后10名中，随机取6个
    last_10 = list(d.items())[-10:]
    random_6 = random.sample(last_10, 6)
    return random_6