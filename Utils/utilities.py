import logging

import softest


class utils(softest.TestCase):

    def softAssert(self, value):
        self.soft_assert(self.assertTrue, value)

    def custom_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        fh = logging.FileHandler(filename='demologger.log')
        logging.basicConfig(filemode='w')
        # formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        ch.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s : %(message)s'))
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger
        # logger.debug('debug: this is debug msg.')
        # logger.info('info: this is info msg.')
        # logger.critical('critical: this is critical msg.')
        # logger.error('error: this is error msg.')
        # logger.warning('warning: this is warning msg.')
