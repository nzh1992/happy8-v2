# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description: 
"""
from flask import Blueprint

from app.models.happy8_number import Happy8NumberModel
from app.models.happy8_prize import (PrizeX10Model, PrizeX9Model, PrizeX8Model, PrizeX7Model, PrizeX6Model,
                                     PrizeX5Model, PrizeX4Model, PrizeX3Model, PrizeX2Model, PrizeX1Model)
from app.models.analyze import ValueModel, NumberCountModel
from app.data_source.data import HistoryData
from app.utils.log import logger


happy8_bp = Blueprint('happy8', __name__, url_prefix="/happy8")


@happy8_bp.route('/update', methods=['POST'])
def happy8_update():
    """
    更新开奖号码、奖金情况
    """


    return "dashboard page."


@happy8_bp.route('/init', methods=['POST'])
def happy8_init():
    """
    初始化开奖号码、奖金情况。仅项目初始化时调用一次。
    """
    # Happy8NumberModel.init_data()

    # Happy8NumberModel.init_prize_data()

    # ValueModel.init_value_analyze()

    NumberCountModel.init_value_count()
    return "dashboard page."
