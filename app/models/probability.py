# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/18
Last Modified: 2025/2/18
Description: 
"""
import math

from app.extentions import db
from app.utils.log import logger
from app.exceptions.system import DatabaseException
from app.data_source.data import HistoryData


class ProbabilityModel(db.Model):
    """快乐8中奖概率表"""
    __tablename__ = 'happy8_number'

    id = db.Column(db.Integer, primary_key=True)
    # 玩法
    name = db.Column(db.String(255), unique=True, nullable=False)
    # 中奖概率
    rate = db.Column(db.Float, nullable=False)
    # 成本
    cost = db.Column(db.Float, nullable=False)
    # 奖金
    bonus = db.Column(db.Float, nullable=False)
    # 描述
    desc = db.Column(db.String(255))

    def __init__(self, name, rate, cost, bonus, desc):
        super().__init__()
        self.name = name
        self.rate = rate
        self.cost = cost
        self.bonus = bonus
        self.desc = desc

    @staticmethod
    def init_data():
        """
        计算并初始化所有快乐8玩法的中奖概率，仅在初始化数据库时调用

        特殊说明:
            1. 后缀s表示单注，后缀c表示复式，后缀d表示胆拖
            2. 奖金bonus，仅保留最高奖金，例如选10奖金500W
        :return:
        """
        model_list = []

        # 1. 选10，单注
        rate = ProbabilityModel._cal_single_rate(10)
        x10_s = ProbabilityModel("选10单注", rate, 2, 5000000, "")
        model_list.append(x10_s)

        # 2. 选9，单注
        rate = ProbabilityModel._cal_single_rate(9)
        x9_s = ProbabilityModel("选9单注", rate, 2, 300000, "")
        model_list.append(x9_s)

        # 3. 选8，单注
        rate = ProbabilityModel._cal_single_rate(8)
        x8_s = ProbabilityModel("选8单注", rate, 2, 50000, "")
        model_list.append(x8_s)

        # 4. 选7，单注
        rate = ProbabilityModel._cal_single_rate(7)
        x7_s = ProbabilityModel("选7单注", rate, 2, 10000, "")
        model_list.append(x7_s)

        # 5. 选6，单注
        rate = ProbabilityModel._cal_single_rate(6)
        x6_s = ProbabilityModel("选6单注", rate, 2, 3000, "")
        model_list.append(x6_s)

        # 6. 选5，单注
        rate = ProbabilityModel._cal_single_rate(5)
        x5_s = ProbabilityModel("选5单注", rate, 2, 1000, "")
        model_list.append(x5_s)

        # 7. 选4，单注
        rate = ProbabilityModel._cal_single_rate(4)
        x4_s = ProbabilityModel("选4单注", rate, 2, 100, "")
        model_list.append(x4_s)

        # 8. 选3，单注
        rate = ProbabilityModel._cal_single_rate(3)
        x3_s = ProbabilityModel("选3单注", rate, 2, 53, "")
        model_list.append(x3_s)

        # 9. 选2，单注
        rate = ProbabilityModel._cal_single_rate(2)
        x2_s = ProbabilityModel("选2单注", rate, 2, 19, "")
        model_list.append(x2_s)

        # 10. 选1，单注
        rate = ProbabilityModel._cal_single_rate(1)
        x1_s = ProbabilityModel("选1单注", rate, 2, 4.6, "")
        model_list.append(x1_s)

        print(model_list)

    @staticmethod
    def _cal_single_rate(pick_number):
        """
        计算单注中奖概率

        :param pick_number: int. 玩法，例如10，表示选10
        :return:
        """
        # 中奖的可能数
        prize_possibilities = math.comb(20, pick_number)

        # 全部的可能数
        all_possibilities = math.comb(80, pick_number)

        rate = prize_possibilities / all_possibilities
        return rate
