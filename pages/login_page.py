from pages.locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.lower().find('login') != -1, "Login is not contains in current url"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_edt = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_edt = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_edt2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_edt.send_keys(email)
        password_edt.send_keys(password)
        password_edt2.send_keys(password)
        register_btn.click()

