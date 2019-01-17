# -*- coding: utf-8 -*-
import logging
import logging.handlers
class Logging():
    def __init__(self, name, filename):
        # 创建名为 spam_application 的记录器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # 创建终端日志处理器
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)

        # 创建时间日志处理器
        self.th = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                           when='midnight', interval=1, backupCount=15,
                                           encoding="utf-8", delay=False, utc=False)
        self.th.setLevel(logging.DEBUG)
        
        # 创建格式器 加到日志处理器中
        self.formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(filename)s(%(lineno)d) %(message)s', '%Y-%m-%d %H:%M:%S')
        self.ch.setFormatter(self.formatter)
        self.th.setFormatter(self.formatter)
    
        self.logger.addHandler(self.ch)
        self.logger.addHandler(self.th)

