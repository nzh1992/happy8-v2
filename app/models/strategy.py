# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/19
Last Modified: 2025/2/19
Description: 
"""
import json
import math
from statistics import median, mean

from app.extentions import db
from app.models.happy8_number import Happy8NumberModel
from app.models.analyze import CurrentMissingModel
from app.utils.log import logger
from app.exceptions.system import DatabaseException


class CatchMissingX2C5Model(db.Model):
    """
    策略名称：
        追最大遗漏

    策略逻辑：
        1. 选2，复式5码。成本20元，中2个19元，中3个57元，中4个114元，中5个190元。
        2. 计算出截止到上一期的最大遗漏号码前5名。
        3. 模拟最大遗漏号码前5名在本期的命中情况，以及投资收益情况
    """
    __tablename__ = 'catch_missing_x2_c5'

    id = db.Column(db.Integer, primary_key=True)
    # 期号
    code = db.Column(db.String(20), unique=True, nullable=False)
    # 玩法
    rule = db.Column(db.String(100))
    # 成本
    cost = db.Column(db.Float, default=0.0)
    # 本期开奖号码
    numbers = db.Column(db.String(255))
    # 投注号码
    bet_numbers = db.Column(db.String(255))
    # 投注号码遗漏情况
    bet_numbers_desc = db.Column(db.String(255))
    # 命中号码
    hit_numbers = db.Column(db.String(255))
    # 奖金
    bonus = db.Column(db.Float, default=0.0)
    # 累计收益
    cumulative_income = db.Column(db.Float, default=0.0)

    def __init__(self, code, number_list, bet_numbers):
        self.code = code
        self.rule = "选2，复式5码"
        self.cost = 20

        bet_numbers_str = [str(i) for i in bet_numbers]
        self.bet_numbers = ",".join(bet_numbers_str)

        self.bet_numbers_desc = json.dumps(CatchMissingX2C5Model.get_bet_numbers_desc(code))

        numbers_str = [str(i) for i in number_list]
        self.numbers = ",".join(numbers_str)

        hit_number_list = self.get_hit_numbers(number_list, bet_numbers)
        hit_numbers_str = [str(i) for i in hit_number_list]

        self.hit_numbers = ",".join(hit_numbers_str)
        self.bonus = self.cal_bonus(hit_number_list)
        self.cumulative_income = self.get_last_cumulative_income() + self.bonus - self.cost

    @staticmethod
    def get_hit_numbers(number_list, bet_numbers):
        """
        计算命中号码
        """
        return list(set.intersection(set(number_list), set(bet_numbers)))

    @staticmethod
    def cal_bonus(hit_number_list):
        """
        计算奖金
        """
        hit_count = len(hit_number_list)
        # 中奖注数
        ticket_count = math.comb(hit_count, 2)
        # 奖金
        bonus = ticket_count * 19
        return bonus

    @staticmethod
    def get_last_cumulative_income():
        """
        获取上一期累计收益
        """
        last_model = CatchMissingX2C5Model.query.order_by(CatchMissingX2C5Model.id.desc()).first()
        if last_model:
            return last_model.cumulative_income
        else:
            return 0

    @staticmethod
    def get_bet_numbers(code):
        """
        获取最大遗漏号码，前5个号码
        """
        # 上一期code
        before_number_model = Happy8NumberModel.get_before_model_by_code(code)

        if before_number_model:
            data_dict = CurrentMissingModel.get_dict(before_number_model.code)
        else:
            # 第一次开奖，没有历史遗漏值查询，给出一组默认值
            data_dict = {"number_1": 0, "number_2": 0, "number_3": 0, "number_4": 0, "number_5": 0}

        sorted_data_list = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
        sorted_data_dict = dict(sorted_data_list[:5])

        bet_numbers = [int(i.split("_")[1]) for i in sorted_data_dict.keys()]
        return bet_numbers

    @staticmethod
    def get_bet_numbers_desc(code):
        """
        获取最大遗漏号码，前5个号码的遗漏详情
        """
        data_dict = CurrentMissingModel.get_dict(code)

        sorted_data_list = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
        sorted_data_dict = dict(sorted_data_list[:5])

        return sorted_data_dict

    @staticmethod
    def init_data():
        """
        初始化数据
        """
        number_models = Happy8NumberModel.query.order_by(Happy8NumberModel.id.asc()).all()

        for number_model in number_models:
            code = number_model.code
            number_list = number_model.get_numbers()
            bet_numbers = CatchMissingX2C5Model.get_bet_numbers(code)
            x2_c5_model = CatchMissingX2C5Model(code, number_list, bet_numbers)

            db.session.add(x2_c5_model)
            db.session.commit()


class HotColdX5C6Model(db.Model):
    """
    策略名称：
        2热+2温+2冷

    策略逻辑：
        1. 选5，复式6码。成本12元。
        2. 计算出2冷、2热、2温码，形成6码组合
        2. 计算出2冷、2热、2温码，形成6码组合
        3. 模拟最大遗漏号码前5名在本期的命中情况，以及投资收益情况
    """
    __tablename__ = 'hot_cold_x5_c6'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)

    # 玩法
    rule = db.Column(db.String(100))
    # 成本
    cost = db.Column(db.Float, default=0.0)
    # 本期开奖号码
    numbers = db.Column(db.String(255))
    # 投注号码
    bet_numbers = db.Column(db.String(255))
    # 投注号码遗漏情况
    bet_numbers_desc = db.Column(db.String(255))
    # 命中号码
    hit_numbers = db.Column(db.String(255))
    # 奖金
    bonus = db.Column(db.Float, default=0.0)
    # 累计收益
    cumulative_income = db.Column(db.Float, default=0.0)

    def __init__(self, code, number_list, bet_numbers):
        self.code = code
        self.rule = "选5，复式6码"
