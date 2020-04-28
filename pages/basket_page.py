from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):        
        self.is_not_element_present(By.CSS_SELECTOR, ".basket-items"), "The product is exist in basket"
        
        
    def should_be_empty_basket_text(self):
        basket_empty_text = self.browser.find_element(By.CSS_SELECTOR, "#content_inner p").text
        print(basket_empty_text)
        except_text = "Your basket is empty. Continue shopping"
        assert  basket_empty_text == except_text, "The basket is not empty"
        