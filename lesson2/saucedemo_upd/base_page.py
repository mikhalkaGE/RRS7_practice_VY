import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import AuthData
from locators import AuthLocators

class BasePage:

    def login(driver, username, password):
        driver.get(AuthData.BASE_URL)
        driver.find_element(By.ID, AuthLocators._username_field).send_keys(username)
        driver.find_element(By.ID, AuthLocators._password_field).send_keys(password)
        driver.find_element(By.ID, AuthLocators._login_button).click() 
