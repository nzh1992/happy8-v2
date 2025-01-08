import pandas as pd

from app import db
from app.utils.log import logger


class RedsModel(db.Model):
    """开奖号码表"""
    __tablename__ = 'reds'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
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

    def get_sum(self):
        """获取本期和值"""
        return sum(self._reds)

    def get_df(self, start_code=None, end_code=None, count=None):
        """
        获取历史数据构成的pd.DataFrame。code为index，red1、red2...red20为column。

        支持两种模式：
        - 通过start_code和end_code获取开始期数和结束期数之间的数据
        - 通过count获取从最近一期开始的count期数据

        :param start_code: str or None. 开始期数，例如'2024100'.
        :param end_code: str or None. 结束期数，例如'2024110'.
        :param count: int or None. 期数
        """
        if start_code and end_code:
            result = RedsModel.query.filter(RedsModel.code.in_(start_code, end_code)).all()
        elif count:
            result = RedsModel.query.order_by(RedsModel.code.desc()).limit(count).all()
        else:
            logger.error(f"参数错误。start_code: {start_code}, end_code: {end_code}, count: {count}")
            raise Exception("参数错误")

        data_list = []
        index_list = []
        column_list = [f"red{i}" for i in range(1, 21)]

        for period in result:
            code = period.code
            index_list.append(code)

            red_list = []
            for i in range(1, 21):
                attr_name = f"red{i}"
                red_list.append(getattr(self, attr_name))

            data_list.append(red_list)

        df = pd.DataFrame(data=data_list, columns=column_list, index=index_list)
        print(df)

        return df


    def __repr__(self):
        return f"<RedsModel id:{self.id} code:{self.code}>"
        