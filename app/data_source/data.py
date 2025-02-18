# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description: 
"""
import json

import requests
import pandas as pd

from app.exceptions.system import ParameterException, CaiPiaoAPIException
from app.utils.log import logger


class HistoryData:
    """
    中国福利彩票中心历史数据
    """
    def __init__(self):
        # 历史数据查询API
        self.history_data_url = "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice"

    @staticmethod
    def _make_history_api_headers():
        """
        构造查询历史数据API的请求头

        :return:
        """
        headers = {
            "Cookie": "HMF_CI=50c2774011b9f462867e5abaadff1245ca4ae4f3fad5563b356191d4088a1a399695cd9f192b80170f76f012e5e7f90e1952f76e7dd3f0c723d2412527c6ee6677; 21_vq=5",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }

        return headers

    @staticmethod
    def _make_history_api_params(page_size):
        """
        构造查询历史数据API的查询参数

        :param page_size: int. 需要查询多少条数据
        :return: dict.
        """
        if not page_size:
            error_info = f"_make_history_params方法page_size参数错误，page_size: {page_size}"
            logger.error(error_info)
            raise ParameterException(error_info)

        params = {
            "name": "kl8",
            "issueCount": "",
            "issueStart": "",
            "issueEnd": "",
            "dayStart": "",
            "dayEnd": "",
            "pageNo": "1",
            "pageSize": str(page_size),
            "week": "",
            "systemType": "PC"
        }

        return params

    def get_data(self, history_count):
        """
        获取历史数据，拿到的是请求接口返回的原始数据

        :param history_count: int. 获取最新一期开始往前的多少期。
        :return: dict.
        """
        if not history_count:
            error_info = f"HistoryData类的get_data方法history_count参数错误，history_count：{history_count}"
            logger.error(error_info)
            raise ParameterException(error_info)

        query_params = self._make_history_api_params(history_count)
        headers = self._make_history_api_headers()

        try:
            resp = requests.get(self.history_data_url, params=query_params, headers=headers, verify=True)
        except Exception as e:
            error_info = f"调用中国福利彩票，获取历史数据API错误，错误信息：{e}"
            logger.error(error_info)
            raise CaiPiaoAPIException(error_info)
        else:
            logger.info("调用中国福利彩票，获取历史数据API成功")
            return json.loads(resp.content)

    def get_prize_data(self, history_count):
        """
        获取中奖信息数据

        :param history_count: int. 获取最新一期开始往前的多少期。
        :return: dict.
        """
        try:
            result = self.get_data(history_count)
            data_list = result.get("result")
            data_list = list(reversed(data_list))

            # 公共数据，仅赋值一次标识
            is_first = True
            public_info = {}

            for data in data_list:
                if is_first:
                    public_info["code"] = data.get("code")
                    public_info["date"] = data.get("date")[10]
                    public_info["pool_money"] = float(data.get("poolmoney"))
                    public_info["sales"] = data.get("sales")
                    public_info["week"] = data.get("week")
                    is_first = False

                prize_data = data.get("prizegrades")

                # 选10



                print(data)
        except Exception as e:
            error_info = f"获取中奖信息错误"
            logger.exception(error_info)
            raise CaiPiaoAPIException(error_info)


    def get_bool_df(self, history_count):
        """
        将统计结果以pd.DataFrame的形式返回，以方便后续统计

        :param history_count: int. 数据的期数
        :return: pd.DataFrame
        """
        content = self.get_data(history_count)
        results = content.get("result")

        index_list = []     # 索引列表
        data_list = []      # 数据列表

        for result in results:
            # 保存索引
            index_list.append(result.get("code"))

            # 保存数据，出现中奖号码为True，未出现为False
            reds = [int(red) for red in result.get("red").split(",")]
            data = [False] * 80
            for red in reds:
                data[red-1] = True

            data_list.append(data)

        # 创建DF
        df = pd.DataFrame(data=data_list, index=index_list, columns=[str(i) for i in range(1, 81)])

        return df

    def get_numbers_df(self, history_count, sort_aesc=False):
        """
        统计结果以pd.DataFrame的形式返回，共21列，第1列是期数，其余20列为开奖号码。

        :param history_count: int. 获取多少期
        :param sort_aesc: bool. 是否排序，若为True，按code升序排列，若为False，按降序排列
        :return:
        """
        content = self.get_data(history_count)
        results = content.get("result")

        data_list = []

        # 定义columns名称
        columns = ['red' + str(i) for i in range(1, 21)]

        # 记录index
        indexes = []

        for result in results:
            # 期数
            code = result.get("code")
            # code作为index
            indexes.append(code)

            # 开奖号码（从小到大排序）
            reds = [int(red) for red in result.get("red").split(",")]
            data_list.append(reds)

        # 创建DF
        df = pd.DataFrame(data=data_list, index=indexes, columns=columns)

        # 是否排序
        if sort_aesc:
            df = df.sort_index()

        return df

    def get_history_count(self):
        """
        获取当前总共历史期数
        """
        data = self.get_data(history_count=1)
        total = data.get("total")
        return total
