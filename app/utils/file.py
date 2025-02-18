# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/2/2
Last Modified: 2025/2/2
Description: 
"""
import os

from app.utils.log import logger


class FileManager:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def create_log_dir(self):
        """
        创建日志目录，位于项目根目录（"<project>/logs"）

        :return:
        """
        log_dir = os.path.join(self.root_dir, 'logs')

        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            logger.info("创建日志目录，成功。")

    def create_output_dir(self):
        """
        创建输出文件存放目录，位于项目根目录（"<project>/output"）
        """
        output_dir = os.path.join(self.root_dir, 'output')

        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
            logger.info("创建文件输出目录，成功。")

    def get_output_dir(self):
        """
        获取输出文件存放目录
        """
        return os.path.join(self.root_dir, 'output')