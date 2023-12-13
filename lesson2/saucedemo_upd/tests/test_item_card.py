import pytest
import time
from data import AuthData, InventoryData
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.item_card_page import ItemCardPage

@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)

@pytest.fixture
def base_page(driver):
    return BasePage(driver)
    
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)
    
@pytest.fixture
def item_card_page(driver):
    return ItemCardPage(driver)

class TestItemCard():

    def test_navigate_to_item_card_by_image(self, base_page, login_page, inventory_page, item_card_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.item_card_image().click()
        time.sleep(3)
        assert item_card_page.driver.current_url == f'{AuthData.BASE_URL}/inventory-item.html?id={InventoryData.item_id}'

    def test_navigate_to_item_card_by_title(self, base_page, login_page, inventory_page, item_card_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.item_card().click()
        time.sleep(3)
        assert item_card_page.driver.current_url == f'{AuthData.BASE_URL}/inventory-item.html?id={InventoryData.item_id}'
