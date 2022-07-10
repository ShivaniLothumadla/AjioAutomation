from selenium.webdriver.common.by import By

from Base.base_driver import BaseDriver
from Pages.search_page import Searchpage


class Homepage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_INPUT_BOX = '[name="searchVal"]'
    SEARCH_SUGGETION_LIST = '[class="rilrtl-list "] li'

    def search_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.SEARCH_INPUT_BOX)

    def products_list(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, self.SEARCH_SUGGETION_LIST)
        return products

    @property
    def result_page(self):
        return Searchpage(self.driver)
