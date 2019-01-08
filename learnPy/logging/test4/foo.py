from logger import Logging

# NOTE: Logger() 为独立对象。name 参数不能带主程序的 logger name，会产生重复对象。
module_logging = Logging('foo','test.log')
module_logger = module_logging.logger

def foo():
    module_logger.info(u'foo.foo 收到一个请求')

if __name__ == '__main__':
    foo()
