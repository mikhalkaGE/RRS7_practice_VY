import pytest
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

class TestFilter():

    def test_filter_a_z(self, base_page, login_page, inventory_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.select_filter('az')
        time.sleep(3)
        assert inventory_page.items_sorting(option='abc', reverse_state=False), 'Sorting A-Z does not work correctly'

    def test_filter_z_a(self, base_page, login_page, inventory_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.select_filter('za')
        time.sleep(3)
        assert inventory_page.items_sorting(option='abc', reverse_state=True), 'Sorting Z-A does not work correctly'

    def test_filter_lo_hi(self, base_page, login_page, inventory_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.select_filter('lohi')
        time.sleep(3)
        assert inventory_page.items_sorting(option='price', reverse_state=False), 'Sorting Price Low-High does not work correctly'

    def test_filter_hi_lo(self, base_page, login_page, inventory_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.select_filter('hilo')
        time.sleep(3)
        assert inventory_page.items_sorting(option='price', reverse_state=True), 'Sorting Price High-Low does not work correctly'
