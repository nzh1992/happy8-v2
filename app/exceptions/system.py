# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description: 
"""


class SystemException(Exception):
    """
    系统异常基类
    """
    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        return f"<SystemException, {self.error_info}>"


class ParameterException(SystemException):
    """
    函数调用参数错误
    """
    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        return f"<ParameterException, {self.error_info}>"


class CaiPiaoAPIException(SystemException):
    """
    调用中国福利彩票API错误
    """
    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        return f"<CaiPiaoAPIException, {self.error_info}>"


class DatabaseException(SystemException):
    """
    数据库操作错误
    """
    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        return f"<DatabaseException, {self.error_info}>"