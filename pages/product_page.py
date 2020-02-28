from pages.locators import ProductPageLocators
import time
from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_product_to_basket()
        self.successfully_adding_product_to_basket_message()
        self.product_price_comparison()



    def add_product_to_basket(self):
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
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert product_name == added_product_name, "Name isn't correct"

    def product_price_comparison(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT).text
        assert product_price == price_alert, "Price isn't correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME), "Success message is not disappeared, but should be"