import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit() 

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=5)
    yield wait
