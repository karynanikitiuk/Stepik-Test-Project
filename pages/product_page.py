from .locators import ProductPageLocators
import time
import math
from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_product_to_basket()
        self.successfully_adding_product_to_basket_message()
        self.second_successfully_message()
        self.product_price_comparison()
        
    def add_product_to_basket(self):
        self.browser.get("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def successfully_adding_product_to_basket_message(self):
        message = self.browser.find_element(*ProductPageLocators.SUCCESSFULL_ADDING_PRODUCT_TO_BASKET_ALERT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text in message.text, "Name isn't correct"
        assert "The shellcoder's handbook has been added to your basket." in message.text, "Message isn't correct"

    def second_successfully_message(self):
        message = self.browser.find_element(*ProductPageLocators.OPPORTUNITY_ALERT)
        assert "Your basket now qualifies for the Deferred benefit offer offer." in message.text, "Message isn't correct"
    
    def product_price_comparison(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT)
        assert product_price.text in price_alert.text, "Price isn't correct"
