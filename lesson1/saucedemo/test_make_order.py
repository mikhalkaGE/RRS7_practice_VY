import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://www.saucedemo.com'
item_id = '4'
item = 'backpack'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_make_order(driver):
    driver.get(BASE_URL)

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

    item_card_title = driver.find_element(By.ID, f'item_{item_id}_title_link')
    assert item_card_title.is_displayed()

    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="checkout"]')
    checkout_button.click()
    assert driver.current_url == f'{BASE_URL}/checkout-step-one.html'

    first_name = driver.find_element(By.XPATH, '//input[@data-test="firstName"]')
    first_name.send_keys('test_first_name')

    last_name = driver.find_element(By.XPATH, '//input[@data-test="lastName"]')
    last_name.send_keys('test_last_name')

    zip_code = driver.find_element(By.XPATH, '//input[@data-test="postalCode"]')
    zip_code.send_keys('80-534')

    time.sleep(3)

    continue_button = driver.find_element(By.XPATH, '//input[@data-test="continue"]')
    continue_button.click()

    assert driver.current_url == f'{BASE_URL}/checkout-step-two.html'

    # StaleElementReferenceException!!!!
    item_card_title = driver.find_element(By.ID, f'item_{item_id}_title_link')
    assert item_card_title.is_displayed()

    time.sleep(3)

    finish_button = driver.find_element(By.XPATH, '//button[@data-test="finish"]')
    finish_button.click()

    assert driver.current_url == f'{BASE_URL}/checkout-complete.html'
    
    ty_banner = driver.find_element(By.CLASS_NAME, 'complete-header')
    assert 'Thank you for your order!' in ty_banner.text

    time.sleep(3)

    back_home_button = driver.find_element(By.XPATH, '//button[@data-test="back-to-products"]')
    back_home_button.click()

    assert driver.current_url == f'{BASE_URL}/inventory.html'

    time.sleep(3)
