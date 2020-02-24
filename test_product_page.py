from pages.main_page import MainPage 
from pages.product_page import ProductPage
from pages.base_page import BasePage

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser) 
    product_page.add_product_to_basket()