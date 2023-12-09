import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

BASE_URL = 'https://www.saucedemo.com'
item_id = '4'
item = 'backpack'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_filter_a_z(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    filter_dd = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    filter_value = Select(filter_dd)
    filter_value.select_by_value('az')

    time.sleep(2)

    items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name ')
    items_list = [item.text for item in items]
    # print(f'\n{items_list}')
    # print(f'\n{sorted(items_list, reverse=True)}')
    assert items_list == sorted(items_list), 'Sorting A-Z does not work correctly'

def test_filter_z_a(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    filter_dd = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    filter_value = Select(filter_dd)
    filter_value.select_by_value('za')

    time.sleep(3)

    items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name ')
    items_list = [item.text for item in items]
    # print(f'\n{items_list}')
    # print(f'\n{sorted(items_list, reverse=True)}')
    assert items_list == sorted(items_list, reverse=True), 'Sorting Z-A does not work correctly'

def test_filter_lo_hi(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    filter_dd = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    filter_value = Select(filter_dd)
    filter_value.select_by_value('lohi')

    time.sleep(3)

    items_prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    items_prices_list = [float(item_price.text.strip('$')) for item_price in items_prices]
    assert items_prices_list == sorted(items_prices_list), 'Sorting Price Low-High does not work correctly'

def test_filter_hi_lo(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    filter_dd = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    filter_value = Select(filter_dd)
    filter_value.select_by_value('hilo')

    time.sleep(3)

    items_prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    items_prices_list = [float(item_price.text.strip('$')) for item_price in items_prices]
    # print(f'\n{items_prices_list}')
    # print(f'\n{sorted(items_prices_list, reverse=True)}')
    assert items_prices_list == sorted(items_prices_list, reverse=True), 'Sorting Price High-Low does not work correctly'
