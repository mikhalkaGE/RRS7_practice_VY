import pytest
from selenium.webdriver.support import expected_conditions as EC
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

class TestCart:

    def test_add_to_cart_from_catalog(self, base_page, login_page, inventory_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.add_to_cart().click()
        assert inventory_page.cart_badge().text == '1'
        assert inventory_page.remove_from_cart().is_displayed()

    def test_remove_from_cart_catalog(self, base_page, login_page, inventory_page, wait):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.add_to_cart().click()
        inventory_page.remove_from_cart().click()
        wait.until_not(EC.presence_of_element_located((inventory_page._cart_badge)))
        # to resolve StaleElementReferenceException:
        assert inventory_page.add_to_cart().is_displayed()

    def test_add_to_cart_from_item_card(self, base_page, login_page, inventory_page, item_card_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.item_card().click()
        assert item_card_page.driver.current_url == f'{AuthData.BASE_URL}/inventory-item.html?id={InventoryData.item_id}'
        item_card_page.add_to_cart().click()
        assert item_card_page.cart_badge().text == '1'
        assert item_card_page.remove_from_cart().is_displayed()

    def test_remove_from_cart_in_item_card(self, base_page, login_page, inventory_page, item_card_page, wait):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.item_card().click()
        assert item_card_page.driver.current_url == f'{AuthData.BASE_URL}/inventory-item.html?id={InventoryData.item_id}'
        item_card_page.add_to_cart().click()
        item_card_page.remove_from_cart().click()
        wait.until_not(EC.presence_of_element_located(inventory_page._cart_badge))
        # to resolve StaleElementReferenceException:
        assert item_card_page.add_to_cart().is_displayed()

    def test_remove_item_from_cart(self, base_page, login_page, inventory_page, item_card_page, wait):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.add_to_cart().click()
        inventory_page.shopping_cart().click()
        item_card_page.remove_from_cart().click()
        wait.until_not(EC.presence_of_element_located(inventory_page._cart_badge))
        wait.until_not(EC.presence_of_element_located(inventory_page._item_card))
