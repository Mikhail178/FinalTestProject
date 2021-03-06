from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find('login') != -1, "Login url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not exist"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not exist"
        
    def register_new_user(self, email, password):
        loginfield = self.browser.find_element(*LoginPageLocators.REGLOGIN_FIELD)
        loginfield.send_keys(email)
        password1Field = self.browser.find_element(*LoginPageLocators.REGPASSWORD1_FIELD)
        password1Field.send_keys(password)
        password2Field = self.browser.find_element(*LoginPageLocators.REGPASSWORD2_FIELD)
        password2Field.send_keys(password)
        regsubmit = self.browser.find_element(*LoginPageLocators.REG_SUBMIT)
        regsubmit.click()
        