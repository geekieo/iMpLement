'''logger解耦，生成多个logger实例'''

from logger import Logging
import foo

logging = Logging('main', 'test.log')
logger = logging.logger

logger.info('main 收到一个请求')

foo.foo()
print(logging.fh.baseFilename)
print(logger.name)