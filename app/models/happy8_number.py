# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description:
"""
from app.extentions import db
from app.utils.log import logger
from app.exceptions.system import DatabaseException
from app.data_source.data import HistoryData


class Happy8NumberModel(db.Model):
    """快乐8开奖号码表"""
    __tablename__ = 'happy8_number'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False, comment="期号")
    red1 = db.Column(db.Integer, nullable=False)
    red2 = db.Column(db.Integer, nullable=False)
    red3 = db.Column(db.Integer, nullable=False)
    red4 = db.Column(db.Integer, nullable=False)
    red5 = db.Column(db.Integer, nullable=False)
    red6 = db.Column(db.Integer, nullable=False)
    red7 = db.Column(db.Integer, nullable=False)
    red8 = db.Column(db.Integer, nullable=False)
    red9 = db.Column(db.Integer, nullable=False)
    red10 = db.Column(db.Integer, nullable=False)
    red11 = db.Column(db.Integer, nullable=False)
    red12 = db.Column(db.Integer, nullable=False)
    red13 = db.Column(db.Integer, nullable=False)
    red14 = db.Column(db.Integer, nullable=False)
    red15 = db.Column(db.Integer, nullable=False)
    red16 = db.Column(db.Integer, nullable=False)
    red17 = db.Column(db.Integer, nullable=False)
    red18 = db.Column(db.Integer, nullable=False)
    red19 = db.Column(db.Integer, nullable=False)
    red20 = db.Column(db.Integer, nullable=False)
    
    def __init__(self, code, reds):
        super().__init__()
        self.code = code
        self._reds = reds

        for idx, red in enumerate(reds):
            attr_name = f"red{idx + 1}"
            setattr(self, attr_name, red)

    def __repr__(self):
        return f"<Happy8Number id:{self.id} code:{self.code}>"

    def get_numbers(self):
        """
        获取开奖号码的list
        """
        return [self.red1, self.red2, self.red3, self.red4, self.red5,
                self.red6, self.red7, self.red8, self.red9, self.red10,
                self.red11, self.red12, self.red13, self.red14, self.red15,
                self.red16, self.red17, self.red18, self.red19, self.red20]

    @staticmethod
    def init_data():
        """
        获取所有开奖号码数据，并存入数据库
        """
        try:
            # 获取总期数
            hd = HistoryData()
            total = hd.get_history_count()
            numbers_df = hd.get_numbers_df(total, sort_aesc=True)

            numbers_model_list = []

            # 序列化
            for row in numbers_df.iterrows():
                code = row[0]
                red_numbers = [item for item in row[1]]
                numbers_model = Happy8NumberModel(code, red_numbers)
                numbers_model_list.append(numbers_model)

            # 保存
            Happy8NumberModel.save_many(model_list=numbers_model_list)
            logger.info(f"初始化完成，共{total}期")
        except Exception as e:
            error_info = f"初始化开奖号码错误，错误信息：{e}"
            logger.exception(error_info)
            raise DatabaseException(error_info)

    @staticmethod
    def init_prize_data():
        """
        获取所有中奖信息数据，并存入数据库
        """
        try:
            # 获取总期数
            hd = HistoryData()
            total = hd.get_history_count()
            numbers_df = hd.get_prize_data(total)

            numbers_model_list = []

            # 序列化
            for row in numbers_df.iterrows():
                code = row[0]
                red_numbers = [item for item in row[1]]
                numbers_model = Happy8NumberModel(code, red_numbers)
                numbers_model_list.append(numbers_model)

            # 保存
            Happy8NumberModel.save_many(model_list=numbers_model_list)
            logger.info(f"初始化完成，共{total}期")
        except Exception as e:
            error_info = f"初始化开奖号码错误，错误信息：{e}"
            logger.exception(error_info)
            raise DatabaseException(error_info)

    @staticmethod
    def save_many(model_list):
        try:
            db.session.add_all(model_list)
        except Exception as e:
            db.session.rollback()

            error_info = f"写入错误：{e}"
            logger.exception(error_info)
            raise DatabaseException(error_info)
        else:
            db.session.commit()
            logger.info("保存成功")
