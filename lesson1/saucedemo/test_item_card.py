import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

BASE_URL = 'https://www.saucedemo.com'
item_id = '4'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_navigate_to_item_card_by_image(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    item_card_image = driver.find_element(By.XPATH, f"//a[@id='item_{item_id}_img_link']/img")
    item_card_image.click()

    time.sleep(3)
    
    assert driver.current_url == f'{BASE_URL}/inventory-item.html?id={item_id}'

def test_navigate_to_item_card_by_title(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    item_card_title = driver.find_element(By.ID, f'item_{item_id}_title_link')
    item_card_title.click()

    time.sleep(3)

    assert driver.current_url == f'{BASE_URL}/inventory-item.html?id={item_id}'
