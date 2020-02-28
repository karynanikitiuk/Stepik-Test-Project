from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Item in basket is presented, but should not be"

    def message_is_shown(self):
        assert self.is_element_present(*BasketPageLocators.NO_ITEMS_MESSAGE), "Message isn't presented, but should be"
   
    def basket_isnt_empty(self):
            assert self.is_element_present(*BasketPageLocators.BASKET_ITEM), "Item in basket isn't presented, but should be"

    def message_isnt_shown(self):
            assert self.is_not_element_present(*BasketPageLocators.NO_ITEMS_MESSAGE), "Message is presented, but should not be"
