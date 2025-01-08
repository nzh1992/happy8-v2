import json

import pandas as pd
import requests


class HistoryData:
    def __init__(self):
        self.base_url = "http://www.cwl.gov.cn"
        self.history_url = "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice"

    def _make_history_params(self, page_size=100, code_start=None, code_end=None):
        """
        两种查询方式（方式2优先）：
            1. 从当前往前page_size期，仅处理page_size参数
            2. 从code_start到code_end期，仅处理code_start和code_end参数
        """
        if code_start and code_end:
            # 方式2
            params = {
                "name": "kl8",
                "issueCount": "",
                "issueStart": code_start,
                "issueEnd": code_end,
                "dayStart": "",
                "dayEnd": "",
                "pageNo": "1",
                "pageSize": "",
                "week": "",
                "systemType": "PC"
            }
        else:
            # 方式1
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

    def _make_history_headers(self):
        headers = {
            "Cookie": "HMF_CI=50c2774011b9f462867e5abaadff1245ca4ae4f3fad5563b356191d4088a1a399695cd9f192b80170f76f012e5e7f90e1952f76e7dd3f0c723d2412527c6ee6677; 21_vq=5",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }

        return headers

    def get_data(self, history_count=None, code_start=None, code_end=None):
        query_params = self._make_history_params(history_count, code_start, code_end)
        headers = self._make_history_headers()

        resp = requests.get(self.history_url, params=query_params, headers=headers, verify=True)

        return json.loads(resp.content)

    def get_df(self, history_count=100):
        """
        将统计结果以pd.DataFrame的形式返回，以方便后续统计

        :param history_count: int. 数据的期数，默认最近100期
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

    def get_reds_df(self, history_count, sort_aesc=False):
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


if __name__ == '__main__':
    h = HistoryData()
    total_period = h.get_history_count()
    data = h.get_data(history_count=total_period)
    print(data)