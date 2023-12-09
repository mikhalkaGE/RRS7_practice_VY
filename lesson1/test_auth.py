import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://www.saucedemo.com'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_form(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == f'{BASE_URL}/inventory.html'

def test_login_form_validation(driver):
    driver.get(BASE_URL)

    validation_text = 'Epic sadface: Username and password do not match any user in this service'

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('user')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(5)

    validation_error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
    assert validation_error.is_displayed(), 'Validation error is not presented!'
    assert validation_text in validation_error.text
