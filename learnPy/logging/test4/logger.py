import logging

class Logging():
    def __init__(self, name, filename):
        # 创建名为 spam_application 的记录器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # 创建级别为 DEBUG 的文件日志处理器
        self.fh = logging.FileHandler(filename, encoding='utf-8')
        self.fh.setLevel(logging.DEBUG)

        # 创建级别为 ERROR 的控制器日志处理器
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)

        # 创建格式器 加到日志处理器中
        self.formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(filename)s line:%(lineno)d] %(message)s', '%Y-%m-%d %H:%M:%S')
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    