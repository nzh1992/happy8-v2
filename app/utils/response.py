# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description: 
"""
def make_response(code, msg, data=None):
    """
    响应数据构造函数

    :param code: int. 错误码
    :param msg: str. 错误信息
    :param data: dict or none. 其他信息，用于传递一些数据信息分析错误，一般为None。
    :return:
    """
    resp = {
        'code': code,
        'msg': msg
    }

    if data is not None:
        resp.update({'data': data})

    return resp