from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        # self.should_be_login_form()
        # self.should_be_register_form()

    def should_be_login_url(self):
        cur_url=self.browser.url
        assert 'login' in cur_url,  "Login link is not opened"
        print("it is login page", cur_url)

    def should_be_login_form(self):
        assert self.browser.is_element_present_by_css(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.is_element_present_by_css(LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self,email,password):
        self.browser.find_by_name(LoginPageLocators.LOGIN_EMAIL).fill(email)
        self.browser.find_by_name(LoginPageLocators.PASSWORD_INPUT).fill(password)
        self.browser.find_by_name(LoginPageLocators.PASSWORD_CONFIRM_INPUT).fill(password)
        self.browser.find_by_name(LoginPageLocators.REGISTER_BUTTON).click()
