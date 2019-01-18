import logger

logging = logger.Logging(name='main', filename='logging')
logging.debug('一个debug信息')

varibale='hello logging '
logging.info('info1 %s'
             'info2'
             'info3',
             varibale)
