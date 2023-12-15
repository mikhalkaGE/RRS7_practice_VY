import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://victoretc.github.io/selenium_waits/'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    yield wait

def test_registration(driver, wait):
    driver.get(url)
    page_title = driver.find_element(By.XPATH, '//h1')
    assert page_title.text == 'Практика с ожиданиями в Selenium'
    begin_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="startTest"]')))
    begin_btn.click()
    login = driver.find_element(By.XPATH, '//input[@id="login"]')
    login.send_keys('login')
    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys('password')
    terms = driver.find_element(By.XPATH, '//input[@id="agree"]')
    terms.click()
    assert terms.is_selected(), 'Terms checkbox was not checked!'
    register_btn = driver.find_element(By.XPATH, '//button[@id="register"]')
    register_btn.click()
    wait.until_not(EC.visibility_of_element_located((By.XPATH, '//div[@id="loader"]')))
    success = driver.find_element(By.XPATH, '//p[@id="successMessage"]')
    assert success.text == 'Вы успешно зарегистрированы!'
    time.sleep(5)
