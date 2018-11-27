from logger import Logger

# NOTE: Logger() 为独立对象。name 参数不能带主程序的 logger name，会产生重复对象。
module_logger = Logger('foo','test.log').logger

def foo():
    module_logger.info(u'foo.foo 收到一个请求')