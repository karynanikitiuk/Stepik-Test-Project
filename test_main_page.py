from pages.main_page import MainPage 
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.locators import BasePageLocators
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, BasePageLocators.HOMEPAGE_LINK)   
        page.open()                      
        page.go_to_login_page()          
        page.should_be_login_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser,  BasePageLocators.HOMEPAGE_LINK)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, BasePageLocators.HOMEPAGE_LINK)   
    page.open()                      
    page.go_to_basket()  
    page.basket_is_empty()
    page.message_is_shown()                    

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, ProductPageLocators.PAGE_LINK_NEW_YEAR)   
    page.open()   
    page.go_to_basket()  
    page.basket_is_empty()
    page.message_is_shown()                    


