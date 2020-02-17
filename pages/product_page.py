from .locators import ProductPageLocators
import time
from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_product_to_basket()
        self.successfully_adding_product_to_basket_message()
        self.product_price_comparison()


    def add_product_to_basket(self):
#        self.browser.get("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
        self.browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

#    def actual_product_name(self):
#        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME) 
#        return product_name
#
#    def basket_product_name(self):       
#        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
#        return added_product_name

    def successfully_adding_product_to_basket_message(self):
        alert_message = self.browser.find_element(*ProductPageLocators.SUCCESSFULL_ADDING_PRODUCT_TO_BASKET_ALERT).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert product_name in added_product_name, "Name isn't correct"

    def product_price_comparison(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT)
        assert product_price.text in price_alert.text, "Price isn't correct"


#from .locators import ProductPageLocators
#import time
#import math
#from selenium.common.exceptions import NoAlertPresentException
#from pages.base_page import BasePage
#from .locators import ProductPageLocators
#
#
#class ProductPage(BasePage):
#    def should_be_product_page(self):
#        self.add_product_to_basket()
#   #    self.actual_product_name()
#   #    self.basket_product_name()
#        self.successfully_adding_product_to_basket_message()
#        self.product_price_comparison()
##        self.second_successfully_message()
#
#
#    def add_product_to_basket(self):
##        self.browser.get("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
#        self.browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
#        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
#        add_to_basket.click()
#        self.solve_quiz_and_get_code()
#
#    def actual_product_name(self):
#        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME) 
#        return product_name
#
#    def basket_product_name(self):       
#        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
#        return added_product_name
#
#    def successfully_adding_product_to_basket_message(self):
##    def successfully_adding_product_to_basket_message(self, product_name, added_product_name):        
#        alert_message = self.browser.find_element(*ProductPageLocators.SUCCESSFULL_ADDING_PRODUCT_TO_BASKET_ALERT).text
#        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
#        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
#        assert product_name in added_product_name, "Name isn't correct"
#        assert "has been added to your basket." in alert_message, "Message isn't correct"
##        assert product_name.text in added_product_name.text, "Message isn't correct"
#
#    def product_price_comparison(self):
#        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
#        price_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT)
#        assert product_price.text in price_alert.text, "Price isn't correct"
#
##    def second_successfully_message(self):
##        message = self.browser.find_element(*ProductPageLocators.OPPORTUNITY_ALERT)
##        assert "Your basket now qualifies for the Deferred benefit offer offer." in message.text, "Message isn't correct"