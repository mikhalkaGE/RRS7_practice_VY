from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    _username_field = (By.ID, 'user-name')
    _password_field = (By.ID, 'password')
    _login_button = (By.ID, 'login-button')
    _validation_error = (By.XPATH, '//h3[@data-test="error"]')

    def login(self, username, password):
        self.driver.find_element(*self._username_field).send_keys(username)
        self.driver.find_element(*self._password_field).send_keys(password)
        self.driver.find_element(*self._login_button).click() 
    
    def validation_error(self):
        return self.driver.find_element(*self._validation_error)
