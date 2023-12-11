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

def test_add_to_cart_from_catalog(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    add_to_cart_button = driver.find_element(By.XPATH, f'//button[@data-test="add-to-cart-sauce-labs-{item}"]')
    add_to_cart_button.click()

    cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == '1'

    remove_from_cart_button = driver.find_element(By.XPATH, f'//button[@data-test="remove-sauce-labs-{item}"]')
    assert remove_from_cart_button.is_displayed()

def test_remove_from_cart_catalog(driver):
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

    time.sleep(3)

    remove_from_cart_button = driver.find_element(By.XPATH, f'//button[@data-test="remove-sauce-labs-{item}"]')
    remove_from_cart_button.click()

    wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, 'shopping_cart_badge')))

    # to resolve StaleElementReferenceException!!!
    add_to_cart_button = driver.find_element(By.XPATH, f'//button[@data-test="add-to-cart-sauce-labs-{item}"]')
    assert add_to_cart_button.is_displayed()

def test_add_to_cart_from_item_card(driver):
    driver.get(BASE_URL)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    item_card = driver.find_element(By.ID, f'item_{item_id}_title_link')
    item_card.click()
    assert driver.current_url == f'{BASE_URL}/inventory-item.html?id={item_id}'

    time.sleep(3)

    add_to_cart_button = driver.find_element(By.XPATH, f'//button[@data-test="add-to-cart-sauce-labs-{item}"]')
    add_to_cart_button.click()

    cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == '1'

    remove_from_cart_button = driver.find_element(By.XPATH, f'//button[@data-test="remove-sauce-labs-{item}"]')
    assert remove_from_cart_button.is_displayed()

def test_remove_from_cart_in_item_card(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 5)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    item_card = driver.find_element(By.ID, f'item_{item_id}_title_link')
    item_card.click()
    assert driver.current_url == f'{BASE_URL}/inventory-item.html?id={item_id}'

    time.sleep(3)

    add_to_cart_button = driver.find_element(By.XPATH, f'//button[@data-test="add-to-cart-sauce-labs-{item}"]')
    add_to_cart_button.click()

    time.sleep(3)

    remove_from_cart_button = driver.find_element(By.XPATH, f'//button[@data-test="remove-sauce-labs-{item}"]')
    remove_from_cart_button.click()

    wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, 'shopping_cart_badge')))

    # to resolve StaleElementReferenceException!!!
    add_to_cart_button = driver.find_element(By.XPATH, f'//button[@data-test="add-to-cart-sauce-labs-{item}"]')
    assert add_to_cart_button.is_displayed()

def test_remove_item_from_cart(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 5)

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(3)

    add_to_cart_button = driver.find_element(By.XPATH, f"//a[@id='item_{item_id}_img_link']/following::button[@data-test='add-to-cart-sauce-labs-{item}']")
    add_to_cart_button.click()

    time.sleep(3)

    shopping_cart_link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    shopping_cart_link.click()

    time.sleep(3)

    remove_from_cart_button = driver.find_element(By.XPATH, f"//a[@id='item_{item_id}_title_link']/following::button[@data-test='remove-sauce-labs-{item}']")
    remove_from_cart_button.click()

    time.sleep(3)

    wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, 'shopping_cart_badge')))
    wait.until_not(EC.presence_of_element_located(((By.ID, f'item_{item_id}_title_link'))))
