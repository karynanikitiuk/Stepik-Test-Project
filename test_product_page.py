from pages.product_page import ProductPage
from .locators import ProductPageLocators

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, ProductPageLocators.PAGE_LINK_NEW_YEAR)
    product_page.open()
    product_page.add_product_to_basket()

