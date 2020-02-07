from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    PASSWORD_RESET_LINK = (By.CSS_SELECTOR, "#login_form > p > a")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#login_form > button")

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    SUCCESSFULL_ADDING_PRODUCT_TO_BASKET_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    OPPORTUNITY_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div")
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, ".col-sm-6.product_main")
    PRODUCT_PRICE_ALERT = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div")
    PRODUCT_NAME = (By.CSS_SELECTOR,  "div.col-sm-6.product_main > h1")
#    PRODUCT_NAME = (By.CSS_SELECTOR,  "#login_form > p > a")

    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")