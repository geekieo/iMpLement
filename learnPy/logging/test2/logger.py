import os
import sys
import logging

class Logger:
    def __init__(self, name, filename):

        # 创建名为 spam_application 的记录器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # 创建级别为 DEBUG 的文件日志处理器
        fh = logging.FileHandler(filename, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 创建级别为 ERROR 的控制器日志处理器
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 创建格式器 加到日志处理器中
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)