from selenium.webdriver.common.by import By

from Base.base_driver import BaseDriver


class Searchpage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    PRODUCTS_LIST = '[class="item rilrtl-products-list__item item"]'
    BRAND = '[class="brand"]'
    NAME = '[class="nameCls"]'
    PRICE = '[class="price  "]'
    ORIGINAL_PRICE = '[class="orginal-price"]'
    DISCOUNT = '[class="discount"]'
    OFFER_PRICE = '[class="offer-pricess"]'

    def products_list(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCTS_LIST)
        return products

    def brand(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.BRAND)

    def name(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.NAME)

    def price(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.PRICE)

    def original_price(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.ORIGINAL_PRICE)

    def discount(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.DISCOUNT)

    def offer_price(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.OFFER_PRICE)

    def product_details(self):
        self.brand()
        self.name()
        self.price()
        self.original_price()
        self.discount()
        self.offer_price()