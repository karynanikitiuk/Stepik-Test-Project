from selenium.webdriver.common.by import By

class BasePageLocators():
    HOMEPAGE_LINK =  "http://selenium1py.pythonanywhere.com/"
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    PAGE_LINK_NEW_YEAR = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PAGE_LINK_NEW_YEAR2 = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    SUCCESSFULL_ADDING_PRODUCT_TO_BASKET_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    OPPORTUNITY_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div")
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")    
    PRODUCT_PRICE_ALERT = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR,  "div.col-sm-6.product_main > h1")
    ADDED_PRODUCT_NAME =  (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR,".basket-items")
    NO_ITEMS_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")