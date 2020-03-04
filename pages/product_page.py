from pages.locators import ProductPageLocators
import time
from pages.base_page import BasePage


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_product_to_basket()
        PRODUCT_NAME = self.actual_product_name()
        PRODUCT_PRICE = self.actual_product_price()
        self.product_price_comparison(PRODUCT_PRICE)
        self.successfully_adding_product_to_basket_message(PRODUCT_NAME)


    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def actual_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name


    def successfully_adding_product_to_basket_message(self, name):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert name == added_product_name, f"Added in basket another product {name}!=={added_product_name}"

    def actual_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def product_price_comparison(self, price):
        price_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT).text
        assert price == price_alert, f"Added in basket pirice not equals to product price{price}!={price_alert}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME), "Success message is not disappeared, but should be"