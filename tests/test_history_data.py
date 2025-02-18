# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description: 测试数据源模块的历史数据功能
"""
import pandas as pd

from app.data_source.data import HistoryData


class TestHistoryData:
    def test_get_data(self):
        """
        测试获取数据方法
        """
        period_count = 5
        data = HistoryData().get_data(period_count)
        assert isinstance(data, dict)
        assert data.get('state') == 0
        assert data.get('message') == "查询成功"

    def test_get_history_count(self):
        """
        测试获取历史数据总期数
        """
        total_count = HistoryData().get_history_count()
        assert isinstance(total_count, int)

    def test_get_bool_df(self):
        """
        测试获取布尔格式的历史数据
        """
        period_count = 5
        bool_df = HistoryData().get_bool_df(period_count)
        assert isinstance(bool_df, pd.DataFrame)

    def test_get_numbers_df(self):
        """
        测试获取数值格式的历史数据
        """
        period_count = 5
        bool_df = HistoryData().get_numbers_df(period_count)
        assert isinstance(bool_df, pd.DataFrame)