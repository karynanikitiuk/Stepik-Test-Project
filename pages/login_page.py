from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
#        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_FIELD), "Login email field is not presented"
#        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "Login password field is not presented"
#        assert self.is_element_present(*LoginPageLocators.PASSWORD_RESET_LINK), "Login password reset link is not presented"
#        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BUTTON), "Login submit button is not presented"
        
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
#        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_FIELD), "Registration email field is not presented"
#        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration password field is not presented"
#        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration repeat password field is not presented"
#        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), "Registration submit button is not presented"
