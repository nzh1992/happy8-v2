# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description: 
"""


class APIException(Exception):
    """
    API异常基类
    """
    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        return f"<APIException, {self.error_info}>"
