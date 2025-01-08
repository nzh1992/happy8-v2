# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/1/5
Last Modified: 2025/1/5
Description: 开奖号码相关转换
"""
from app.models.reds import RedsModel


class RedsTransfer:
    def __init__(self, reds_df):
        self.reds_df = reds_df

    def to_reds_model_list(self):
        """
        将pd.DataFrame转换为RedsModel对象
        """
        reds_model_list = []

        for row in self.reds_df.iterrows():
            code = row[0]
            red_numbers = [item for item in row[1]]
            red_model = RedsModel(code, red_numbers)
            reds_model_list.append(red_model)

        return reds_model_list
