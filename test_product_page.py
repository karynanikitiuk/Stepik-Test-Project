from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.locators import BasePageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time
import pytest

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, BasePageLocators.LOGIN_URL)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "password[/}")
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product = ProductPage(browser, ProductPageLocators.PAGE_LINK_NEW_YEAR)
        product.open()
        product.should_be_product_page()
    
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLocators.PAGE_LINK_NEW_YEAR)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PAGE_LINK_NEW_YEAR)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PAGE_LINK_NEW_YEAR)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, ProductPageLocators.PAGE_LINK_NEW_YEAR)   
    page.open()   
    page.go_to_basket()  
    page.basket_is_empty()
    page.message_is_shown()                    

