import pytest
import time
from data import AuthData
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

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
def cart_page(driver):
    return CartPage(driver)

class TestMakeOrder:

    def test_make_order(self, base_page, login_page, inventory_page, cart_page):

        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        inventory_page.add_to_cart().click()
        inventory_page.shopping_cart().click()
        assert cart_page.item_card().is_displayed()
        cart_page.checkout_button().click()
        assert cart_page.driver.current_url == f'{AuthData.BASE_URL}/checkout-step-one.html'
        cart_page.first_name().send_keys('test_first_name')
        cart_page.last_name().send_keys('test_last_name')
        cart_page.zip_code().send_keys('80-534')
        cart_page.continue_button().click()
        assert cart_page.driver.current_url == f'{AuthData.BASE_URL}/checkout-step-two.html'
        assert cart_page.item_card().is_displayed()
        cart_page.finish_button().click()
        assert cart_page.driver.current_url == f'{AuthData.BASE_URL}/checkout-complete.html'
        assert 'Thank you for your order!' in cart_page.ty_banner().text
        cart_page.back_home().click()
        assert cart_page.driver.current_url == f'{AuthData.BASE_URL}/inventory.html'
        time.sleep(3)
