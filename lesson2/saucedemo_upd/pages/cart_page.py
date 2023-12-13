from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

class CartPage(InventoryPage):

    _checkout_button = (By.XPATH, '//button[@data-test="checkout"]')
    _first_name = (By.XPATH, '//input[@data-test="firstName"]')
    _last_name = (By.XPATH, '//input[@data-test="lastName"]')
    _zip_code = (By.XPATH, '//input[@data-test="postalCode"]')
    _continue_button = (By.XPATH, '//input[@data-test="continue"]')
    _finish_button = (By.XPATH, '//button[@data-test="finish"]')
    _ty_banner = (By.CLASS_NAME, 'complete-header')
    _back_home_button = (By.XPATH, '//button[@data-test="back-to-products"]')


    def checkout_button(self):
        return self.driver.find_element(*self._checkout_button)
    
    def first_name(self):
        return self.driver.find_element(*self._first_name)
    
    def last_name(self):
        return self.driver.find_element(*self._last_name)
    
    def zip_code(self):
        return self.driver.find_element(*self._zip_code)
    
    def continue_button(self):
        return self.driver.find_element(*self._continue_button)
    
    def finish_button(self):
        return self.driver.find_element(*self._finish_button)
    
    def ty_banner(self):
        return self.driver.find_element(*self._ty_banner)
    
    def back_home(self):
        return self.driver.find_element(*self._back_home_button)
