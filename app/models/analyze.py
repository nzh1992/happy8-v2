# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/18
Last Modified: 2025/2/18
Description: 
"""
from statistics import median, mean

from app.extentions import db
from app.models.happy8_number import Happy8NumberModel
from app.utils.log import logger
from app.exceptions.system import DatabaseException


class ValueModel(db.Model):
    """开奖号码的数值表现"""
    __tablename__ = 'value_analyze'

    id = db.Column(db.Integer, primary_key=True)
    # 期号
    code = db.Column(db.String(20), unique=True, nullable=False)
    # 平均值
    ave = db.Column(db.Float)
    # 最大值
    max = db.Column(db.Float)
    # 最小值
    min = db.Column(db.Float)
    # 中位数
    mid = db.Column(db.Float)
    # 奇数个数
    odd_count = db.Column(db.Integer)
    # 偶数个数
    even_count = db.Column(db.Integer)
    # 大数个数（大于40）
    big_number_count = db.Column(db.Integer)
    # 小数个数（小于等于40）
    small_number_count = db.Column(db.Integer)
    # 1区个数（号码1~8）
    area1_count = db.Column(db.Integer)
    # 2区个数（号码9~16）
    area2_count = db.Column(db.Integer)
    # 3区个数（号码17~24）
    area3_count = db.Column(db.Integer)
    # 4区个数（号码25~32）
    area4_count = db.Column(db.Integer)
    # 5区个数（号码33~40）
    area5_count = db.Column(db.Integer)
    # 6区个数（号码41~48）
    area6_count = db.Column(db.Integer)
    # 7区个数（号码49~56）
    area7_count = db.Column(db.Integer)
    # 8区个数（号码57~64）
    area8_count = db.Column(db.Integer)
    # 9区个数（号码65~72）
    area9_count = db.Column(db.Integer)
    # 10区个数（号码73~80）
    area10_count = db.Column(db.Integer)

    def __init__(self, code, number_list):
        self.code = code
        self.ave = mean(number_list)
        self.max = max(number_list)
        self.min = min(number_list)
        self.mid = median(number_list)
        self.odd_count = self._get_odd_count(number_list)
        self.even_count = self._get_even_count(number_list)
        self.big_number_count = self._get_big_number_count(number_list)
        self.small_number_count = self._get_small_number_count(number_list)
        self.area1_count = self._get_area_count(1, number_list)
        self.area2_count = self._get_area_count(2, number_list)
        self.area3_count = self._get_area_count(3, number_list)
        self.area4_count = self._get_area_count(4, number_list)
        self.area5_count = self._get_area_count(5, number_list)
        self.area6_count = self._get_area_count(6, number_list)
        self.area7_count = self._get_area_count(7, number_list)
        self.area8_count = self._get_area_count(8, number_list)
        self.area9_count = self._get_area_count(9, number_list)
        self.area10_count = self._get_area_count(10, number_list)

    def _get_odd_count(self, number_list):
        """
        计算奇数个数
        """
        odd_numbers = [i for i in number_list if i % 2 == 1]
        return len(odd_numbers)

    def _get_even_count(self, number_list):
        """
        计算偶数个数
        """
        even_numbers = [i for i in number_list if i % 2 == 0]
        return len(even_numbers)

    def _get_big_number_count(self, number_list):
        """
        计算大数个数（大于40）
        """
        big_numbers = [i for i in number_list if i > 40]
        return len(big_numbers)

    def _get_small_number_count(self, number_list):
        """
        计算小数个数（小于等于40）
        """
        small_numbers = [i for i in number_list if i <= 40]
        return len(small_numbers)

    def _get_area_count(self, area_number, number_list):
        """
        计算某一分区出现号码的个数
        """
        if area_number < 1 or area_number > 10:
            return Exception("area_number取值范围错误")

        start = (area_number - 1) * 8 + 1
        end = area_number * 8

        area_numbers = [i for i in number_list if start <= i <= end]
        return len(area_numbers)

    @staticmethod
    def init_value_analyze():
        """
        初始化数值分析表
        """
        value_model_list = []

        all_period = Happy8NumberModel.query.order_by("code").all()
        for number_model in all_period:
            code = number_model.code
            number_list = number_model.get_numbers()
            value_model = ValueModel(code, number_list)
            value_model_list.append(value_model)

        db.session.add_all(value_model_list)
        db.session.commit()


class NumberCountModel(db.Model):
    """
    号码出现次数表
    """
    __tablename__ = 'number_count'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    number_1 = db.Column(db.Integer, default=0)
    number_2 = db.Column(db.Integer, default=0)
    number_3 = db.Column(db.Integer, default=0)
    number_4 = db.Column(db.Integer, default=0)
    number_5 = db.Column(db.Integer, default=0)
    number_6 = db.Column(db.Integer, default=0)
    number_7 = db.Column(db.Integer, default=0)
    number_8 = db.Column(db.Integer, default=0)
    number_9 = db.Column(db.Integer, default=0)
    number_10 = db.Column(db.Integer, default=0)
    number_11 = db.Column(db.Integer, default=0)
    number_12 = db.Column(db.Integer, default=0)
    number_13 = db.Column(db.Integer, default=0)
    number_14 = db.Column(db.Integer, default=0)
    number_15 = db.Column(db.Integer, default=0)
    number_16 = db.Column(db.Integer, default=0)
    number_17 = db.Column(db.Integer, default=0)
    number_18 = db.Column(db.Integer, default=0)
    number_19 = db.Column(db.Integer, default=0)
    number_20 = db.Column(db.Integer, default=0)
    number_21 = db.Column(db.Integer, default=0)
    number_22 = db.Column(db.Integer, default=0)
    number_23 = db.Column(db.Integer, default=0)
    number_24 = db.Column(db.Integer, default=0)
    number_25 = db.Column(db.Integer, default=0)
    number_26 = db.Column(db.Integer, default=0)
    number_27 = db.Column(db.Integer, default=0)
    number_28 = db.Column(db.Integer, default=0)
    number_29 = db.Column(db.Integer, default=0)
    number_30 = db.Column(db.Integer, default=0)
    number_31 = db.Column(db.Integer, default=0)
    number_32 = db.Column(db.Integer, default=0)
    number_33 = db.Column(db.Integer, default=0)
    number_34 = db.Column(db.Integer, default=0)
    number_35 = db.Column(db.Integer, default=0)
    number_36 = db.Column(db.Integer, default=0)
    number_37 = db.Column(db.Integer, default=0)
    number_38 = db.Column(db.Integer, default=0)
    number_39 = db.Column(db.Integer, default=0)
    number_40 = db.Column(db.Integer, default=0)
    number_41 = db.Column(db.Integer, default=0)
    number_42 = db.Column(db.Integer, default=0)
    number_43 = db.Column(db.Integer, default=0)
    number_44 = db.Column(db.Integer, default=0)
    number_45 = db.Column(db.Integer, default=0)
    number_46 = db.Column(db.Integer, default=0)
    number_47 = db.Column(db.Integer, default=0)
    number_48 = db.Column(db.Integer, default=0)
    number_49 = db.Column(db.Integer, default=0)
    number_50 = db.Column(db.Integer, default=0)
    number_51 = db.Column(db.Integer, default=0)
    number_52 = db.Column(db.Integer, default=0)
    number_53 = db.Column(db.Integer, default=0)
    number_54 = db.Column(db.Integer, default=0)
    number_55 = db.Column(db.Integer, default=0)
    number_56 = db.Column(db.Integer, default=0)
    number_57 = db.Column(db.Integer, default=0)
    number_58 = db.Column(db.Integer, default=0)
    number_59 = db.Column(db.Integer, default=0)
    number_60 = db.Column(db.Integer, default=0)
    number_61 = db.Column(db.Integer, default=0)
    number_62 = db.Column(db.Integer, default=0)
    number_63 = db.Column(db.Integer, default=0)
    number_64 = db.Column(db.Integer, default=0)
    number_65 = db.Column(db.Integer, default=0)
    number_66 = db.Column(db.Integer, default=0)
    number_67 = db.Column(db.Integer, default=0)
    number_68 = db.Column(db.Integer, default=0)
    number_69 = db.Column(db.Integer, default=0)
    number_70 = db.Column(db.Integer, default=0)
    number_71 = db.Column(db.Integer, default=0)
    number_72 = db.Column(db.Integer, default=0)
    number_73 = db.Column(db.Integer, default=0)
    number_74 = db.Column(db.Integer, default=0)
    number_75 = db.Column(db.Integer, default=0)
    number_76 = db.Column(db.Integer, default=0)
    number_77 = db.Column(db.Integer, default=0)
    number_78 = db.Column(db.Integer, default=0)
    number_79 = db.Column(db.Integer, default=0)
    number_80 = db.Column(db.Integer, default=0)

    def __init__(self, code, number_list, last_model):
        self.code = code
        self.last_model = last_model

        for number in range(1, 81):
            attr_name = f"number_{number}"
            last_count = getattr(last_model, attr_name, 0)

            if number in number_list:
                setattr(self, attr_name, last_count + 1)
            else:
                setattr(self, attr_name, last_count)

    @staticmethod
    def init_value_count():
        number_models = Happy8NumberModel.query.order_by("id").all()

        for number_model in number_models:
            code = number_model.code
            number_list = number_model.get_numbers()

            last_number_model = Happy8NumberModel.query.filter_by(id=number_model.id - 1).first()
            if last_number_model:
                last_model = NumberCountModel.query.filter_by(code=last_number_model.code).first()
            else:
                last_model = None

            count_model = NumberCountModel(code, number_list, last_model)
            db.session.add(count_model)
            db.session.commit()