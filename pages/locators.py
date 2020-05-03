from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class LoginPageLocators():    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    REGLOGIN_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGPASSWORD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGPASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, ".btn-primary[name='login_submit']")
    REG_SUBMIT = (By.CSS_SELECTOR, ".btn-primary[name='registration_submit']")
    
class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-safe:first-child")
    