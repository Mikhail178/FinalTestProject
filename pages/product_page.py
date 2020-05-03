from .base_page import BasePage
from .basket_page import BasketPage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
        add_to_basket_button.click()
 
    def should_be_product_added_to_basket_alert(self):
        product_text = self.browser.find_element(By.CSS_SELECTOR, ".col-sm-6.product_main h1").text
        alert_text = self.browser.find_element(By.CSS_SELECTOR, ".alertinner strong").text
        assert  product_text == alert_text, "The product is not added in basket"
    
    def should_be_basket_price_equals_product_price(self):
        basket_price = self.browser.find_element(By.CSS_SELECTOR, ".alertinner p strong").text
        product_price = self.browser.find_element(By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color").text        
        assert basket_price == product_price, "prices is not equals"
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)        
        alert.accept()
        try:
            alert = self.browser.switch_to.alert            
            alert_text = alert.text
            print(f"Your code: {alert_text}")            
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
       
    def should_be_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "The element is presented, but should not be"
        