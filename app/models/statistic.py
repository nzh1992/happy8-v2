# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/1/4
Last Modified: 2025/1/4
Description: 
"""
from app import db
from app.utils.log import logger


class ValueStatisticModel(db.Model):
    """数值统计表"""
    __tablename__ = 'stat_value'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    sum = db.Column(db.Integer, nullable=False)         # 和值
    ave = db.Column(db.Float, nullable=False)           # 均值
    odd_count = db.Column(db.Integer, nullable=False)   # 奇数个数
    even_count = db.Column(db.Integer, nullable=False)  # 偶数个数

    def __init__(self, code, sum, ave, odd_count, even_count):
        super().__init__()
        self.code = code
        self.sum = sum
        self.ave = ave
        self.odd_count = odd_count
        self.even_count = even_count


class RedCountStatisticModel(db.Model):
    """号码出现次数统计"""
    __tablename__ = 'stat_red_count'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    red_1 = db.Column(db.Integer, nullable=False, default=0)  # 号码1出现的次数
    red_2 = db.Column(db.Integer, nullable=False, default=0)
    red_3 = db.Column(db.Integer, nullable=False, default=0)
    red_4 = db.Column(db.Integer, nullable=False, default=0)
    red_5 = db.Column(db.Integer, nullable=False, default=0)
    red_6 = db.Column(db.Integer, nullable=False, default=0)
    red_7 = db.Column(db.Integer, nullable=False, default=0)
    red_8 = db.Column(db.Integer, nullable=False, default=0)
    red_9 = db.Column(db.Integer, nullable=False, default=0)
    red_10 = db.Column(db.Integer, nullable=False, default=0)
    red_11 = db.Column(db.Integer, nullable=False, default=0)
    red_12 = db.Column(db.Integer, nullable=False, default=0)
    red_13 = db.Column(db.Integer, nullable=False, default=0)
    red_14 = db.Column(db.Integer, nullable=False, default=0)
    red_15 = db.Column(db.Integer, nullable=False, default=0)
    red_16 = db.Column(db.Integer, nullable=False, default=0)
    red_17 = db.Column(db.Integer, nullable=False, default=0)
    red_18 = db.Column(db.Integer, nullable=False, default=0)
    red_19 = db.Column(db.Integer, nullable=False, default=0)
    red_20 = db.Column(db.Integer, nullable=False, default=0)
    red_21 = db.Column(db.Integer, nullable=False, default=0)
    red_22 = db.Column(db.Integer, nullable=False, default=0)
    red_23 = db.Column(db.Integer, nullable=False, default=0)
    red_24 = db.Column(db.Integer, nullable=False, default=0)
    red_25 = db.Column(db.Integer, nullable=False, default=0)
    red_26 = db.Column(db.Integer, nullable=False, default=0)
    red_27 = db.Column(db.Integer, nullable=False, default=0)
    red_28 = db.Column(db.Integer, nullable=False, default=0)
    red_29 = db.Column(db.Integer, nullable=False, default=0)
    red_30 = db.Column(db.Integer, nullable=False, default=0)
    red_31 = db.Column(db.Integer, nullable=False, default=0)
    red_32 = db.Column(db.Integer, nullable=False, default=0)
    red_33 = db.Column(db.Integer, nullable=False, default=0)
    red_34 = db.Column(db.Integer, nullable=False, default=0)
    red_35 = db.Column(db.Integer, nullable=False, default=0)
    red_36 = db.Column(db.Integer, nullable=False, default=0)
    red_37 = db.Column(db.Integer, nullable=False, default=0)
    red_38 = db.Column(db.Integer, nullable=False, default=0)
    red_39 = db.Column(db.Integer, nullable=False, default=0)
    red_40 = db.Column(db.Integer, nullable=False, default=0)
    red_41 = db.Column(db.Integer, nullable=False, default=0)
    red_42 = db.Column(db.Integer, nullable=False, default=0)
    red_43 = db.Column(db.Integer, nullable=False, default=0)
    red_44 = db.Column(db.Integer, nullable=False, default=0)
    red_45 = db.Column(db.Integer, nullable=False, default=0)
    red_46 = db.Column(db.Integer, nullable=False, default=0)
    red_47 = db.Column(db.Integer, nullable=False, default=0)
    red_48 = db.Column(db.Integer, nullable=False, default=0)
    red_49 = db.Column(db.Integer, nullable=False, default=0)
    red_50 = db.Column(db.Integer, nullable=False, default=0)
    red_51 = db.Column(db.Integer, nullable=False, default=0)
    red_52 = db.Column(db.Integer, nullable=False, default=0)
    red_53 = db.Column(db.Integer, nullable=False, default=0)
    red_54 = db.Column(db.Integer, nullable=False, default=0)
    red_55 = db.Column(db.Integer, nullable=False, default=0)
    red_56 = db.Column(db.Integer, nullable=False, default=0)
    red_57 = db.Column(db.Integer, nullable=False, default=0)
    red_58 = db.Column(db.Integer, nullable=False, default=0)
    red_59 = db.Column(db.Integer, nullable=False, default=0)
    red_60 = db.Column(db.Integer, nullable=False, default=0)
    red_61 = db.Column(db.Integer, nullable=False, default=0)
    red_62 = db.Column(db.Integer, nullable=False, default=0)
    red_63 = db.Column(db.Integer, nullable=False, default=0)
    red_64 = db.Column(db.Integer, nullable=False, default=0)
    red_65 = db.Column(db.Integer, nullable=False, default=0)
    red_66 = db.Column(db.Integer, nullable=False, default=0)
    red_67 = db.Column(db.Integer, nullable=False, default=0)
    red_68 = db.Column(db.Integer, nullable=False, default=0)
    red_69 = db.Column(db.Integer, nullable=False, default=0)
    red_70 = db.Column(db.Integer, nullable=False, default=0)
    red_71 = db.Column(db.Integer, nullable=False, default=0)
    red_72 = db.Column(db.Integer, nullable=False, default=0)
    red_73 = db.Column(db.Integer, nullable=False, default=0)
    red_74 = db.Column(db.Integer, nullable=False, default=0)
    red_75 = db.Column(db.Integer, nullable=False, default=0)
    red_76 = db.Column(db.Integer, nullable=False, default=0)
    red_77 = db.Column(db.Integer, nullable=False, default=0)
    red_78 = db.Column(db.Integer, nullable=False, default=0)
    red_79 = db.Column(db.Integer, nullable=False, default=0)
    red_80 = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, code, red_list):
        super().__init__()
        self.code = code

    def _red_list_to_attr(self):
        """"""