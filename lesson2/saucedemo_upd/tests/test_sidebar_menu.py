import pytest
from selenium.webdriver.support import expected_conditions as EC
import time
from data import AuthData
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)

@pytest.fixture
def base_page(driver):
    return BasePage(driver)
    
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

class TestSidebarMenu:

    #TODO remove time.sleep()

    def test_logout(self, base_page, login_page, inventory_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.burger_menu().click()
        time.sleep(3)
        inventory_page.logout().click()
        assert login_page.driver.current_url == f'{AuthData.BASE_URL}/'

    def test_about(self, base_page, login_page, inventory_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.burger_menu().click()
        time.sleep(3)
        inventory_page.about().click()
        assert inventory_page.driver.current_url == 'https://saucelabs.com/'

    def test_reset_app_state(self, base_page, login_page, inventory_page, wait):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.add_to_cart().click()
        inventory_page.burger_menu().click()
        time.sleep(3)
        inventory_page.reset().click()
        #TODO Figure out with assets:
        wait.until_not(EC.presence_of_element_located(inventory_page._cart_badge))
        wait.until(EC.presence_of_element_located(inventory_page._add_to_cart_button))
