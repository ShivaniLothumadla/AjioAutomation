from time import sleep

import softest
import logging
import pytest
from Pages.homepage import Homepage
from Utils.utilities import utils
from ddt import ddt, unpack, file_data, data

@ddt
@pytest.mark.usefixtures("setup")
class HomePage(softest.TestCase):
    # logging.basicConfig(level=logging.DEBUG, filename='..\Logging\loggersconfig.log', filemode='w', format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = Homepage(self.driver)
        self.ut = utils()

    # @data(('Shoes', ))
    # @unpack
    @file_data('../testdata/test.json')
    def test_home_page(self, product1):
        print('this is print stmnt')
        logging.warning('this is first warning logger stmnt')
        self.hp.search_input().click()
        products = self.hp.products_list()
        for product in products:
            if product.text == product1:
                sleep(20)
                product.click()
                break
        self.hp.result_page.brand()
        self.hp.result_page.scroll_to_we()
        # products = self.hp.result_page.products_list()
        # brand = self.hp.result_page.brand()
        # name = self.hp.result_page.name()
        # price = self.hp.result_page.price()
        # original_price = self.hp.result_page.original_price()
        # discount = self.hp.result_page.discount()
        # offer_price = self.hp.result_page.offer_price()
        # self.hp.result_page.product_details()
        # for product in range(len(products)):
        #     self.ut.softAssert(products[product].text)
        #     # self.soft_assert(self.assertTrue, products[product].text)
        #     log = self.ut.custom_logger()
        #     log.info('warning: {}'.format(products[product].text))
        #     self.ut.softAssert(brand[product].text)
        #     log.info('error: {}'.format(brand[product].text))
        #     self.ut.softAssert(self.assertTrue)
        #     log.info('critical: {}'.format(name[product].text))
        #     self.ut.softAssert(price[product].text)
        #     log.info('warning: {}'.format(price[product].text))
        #     try:
        #         self.soft_assert(self.assertTrue, original_price)
        #         self.assertTrue(original_price[product].text, msg=f'{original_price[product].text} is not displayed')
        #         log.info('warning: {}'.format(original_price[product].text))
        #         if discount[product].text == '':
        #             self.assertTrue(discount[product].text, msg=f'{discount[product].text} is not displayed')
        #             log.info('warning: {}'.format(discount[product].text))
        #         if offer_price[product].text == '':
        #             self.assertTrue(offer_price[product].text, msg=f'{offer_price[product].text} is not displayed')
        #             log.info('warning: {}'.format(offer_price[product].text))
        #     except Exception:
        #         continue