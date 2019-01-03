'''使用一个logger实例'''

import logging
import auxiliary

# 创建名为 spam_application 的记录器
logger = logging.getLogger('application')
logger.setLevel(logging.DEBUG)

# 创建级别为 DEBUG 的文件日志处理器
fh = logging.FileHandler('spam.log', encoding='utf-8')
fh.setLevel(logging.DEBUG)

# 创建级别为 ERROR 的控制器日志处理器
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 创建格式器 加到日志处理器中
formatter = logging.Formatter(
    '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s', '%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.info('main 收到一个请求')
# logger.info('creating an instance of auxiliary.Auxiliary')
# a = auxiliary.Auxiliary()
# logger.info('created an instance of auxiliar.Auxiliary')
# logger.info('calling auxiliary.Auxiliary.aux_foo')
# a.aux_foo()
# logger.info('done with auxiliary.Auxiliary.aux_foo')
# logger.info('calling auxiliary.foo()')
auxiliary.foo()
# logger.info('done with auxiliary.foo()')

