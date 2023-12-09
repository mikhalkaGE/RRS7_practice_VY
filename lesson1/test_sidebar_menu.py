import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

BASE_URL = 'https://www.saucedemo.com'
item_id = '4'
item = 'backpack'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_logout(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    burger_menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu_button.click()

    time.sleep(3)

    logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
    logout_button.click()

    time.sleep(3)

    assert driver.current_url == f'{BASE_URL}/'

def test_about(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    burger_menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu_button.click()

    time.sleep(3)

    about_button = driver.find_element(By.ID, 'about_sidebar_link')
    about_button.click()

    time.sleep(3)

    assert driver.current_url == 'https://saucelabs.com/'

def test_reset_app_state(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 5)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    add_to_cart_button = driver.find_element(By.XPATH, f'//button[@data-test="add-to-cart-sauce-labs-{item}"]')
    add_to_cart_button.click()

    burger_menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu_button.click()

    time.sleep(3)

    reset_button = driver.find_element(By.ID, 'reset_sidebar_link')
    reset_button.click()

    time.sleep(3)

    #TODO Figure out with assets:
    wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, 'shopping_cart_badge')))
    wait.until(EC.presence_of_element_located((By.XPATH, f'//button[@data-test="add-to-cart-sauce-labs-{item}"]')))
