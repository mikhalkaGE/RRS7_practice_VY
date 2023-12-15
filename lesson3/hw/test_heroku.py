import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

url = 'https://the-internet.herokuapp.com/'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 5)
    yield wait

def test_add_remove_element(driver, wait):
    driver.get(f'{url}add_remove_elements/')
    add_element_btn = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
    add_element_btn.click()
    delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Delete"]')))
    delete_btn.click()
    wait.until_not(EC.visibility_of_element_located((By.XPATH, '//button[text()="Delete"]')))
    #TODO assert with is_displayed() method is unavailable because of stale webelement exeption

def test_basic_auth(driver, wait):
    username = 'admin'
    password = 'admin'
    driver.get(f'http://{username}:{password}@the-internet.herokuapp.com/basic_auth/')
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//div[@class="example"]/p'), 'Congratulations!'))

def test_broken_image(driver):
    driver.get(f'{url}/broken_images')
    imgs = driver.find_elements(By.TAG_NAME, 'img')
    for img in imgs:
        img_src = img.get_attribute('src')
        src_responce = requests.get(img_src)
        # if src_responce.status_code != 200:
        #     return img_src
        assert src_responce.status_code == 200, f'Image {img_src} is broken!'
