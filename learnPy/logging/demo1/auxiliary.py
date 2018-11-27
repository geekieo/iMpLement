import logging
# NOTE: getLogger() 的 name 参数必须带主程序的 logger name,并用 . 连接主程序 name 和子程序 name。
module_logger = logging.getLogger('application.auxiliary')

class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
        self.logger.info("creating an instance of Auxiliary")

    def aux_foo(self):
        self.logger.info('doing something')
        a = 1+1
        self.logger.info('done doing something')
        
def foo():
    module_logger.info(u'foo 收到一个请求')