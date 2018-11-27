'''logger解耦，生成多个logger实例'''

from logger import Logger
import foo

logger = Logger('main', 'test.log').logger
logger.info('main 收到一个请求')

foo.foo()