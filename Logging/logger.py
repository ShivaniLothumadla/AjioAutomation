#create logger
#create console or file logger and set level
#add format
#add format to console or file logger
#add console or file logger to created logger
import logging

class LoggerDemo:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    fh = logging.FileHandler(filename='demologger.log')
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
    ch.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s : %(message)s'))
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.debug('debug: this is debug msg.')
    logger.info('info: this is info msg.')
    logger.critical('critical: this is critical msg.')
    logger.error('error: this is error msg.')
    logger.warning('warning: this is warning msg.')