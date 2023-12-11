from selenium.webdriver.common.by import By
import time
from locators import AuthLocators
from data import AuthData
from base_page import BasePage

def test_login_form(driver):
    BasePage.login(driver, AuthData.LOGIN, AuthData.PASSWORD)
    time.sleep(2)
    assert driver.current_url == f'{AuthData.BASE_URL}/inventory.html'

def test_login_form_validation(driver):
    BasePage.login(driver, AuthData.INVALID_LOGIN, AuthData.INVALID_PASSWORD)
    time.sleep(2)
    assert (driver.find_element(By.XPATH, AuthLocators._validation_error)).is_displayed(), 'Validation error is not presented!'
    assert AuthData.AUTH_ERROR in (driver.find_element(By.XPATH, AuthLocators._validation_error)).text
