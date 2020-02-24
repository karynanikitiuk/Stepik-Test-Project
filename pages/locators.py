from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
#    LOGIN_USERNAME_FIELD = (By.CSS_SELECTOR, "#id_login-username")
#    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
#    PASSWORD_RESET_LINK = (By.CSS_SELECTOR, "#login_form > p > a")
#    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#login_form > button")

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
#    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
#    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
#    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
#    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    PAGE_LINK_NEW_YEAR = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#    PAGE_LINK_NEW_YEAR = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    SUCCESSFULL_ADDING_PRODUCT_TO_BASKET_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    OPPORTUNITY_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div")
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    
    PRODUCT_PRICE_ALERT = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR,  "div.col-sm-6.product_main > h1")
    ADDED_PRODUCT_NAME =  (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")

