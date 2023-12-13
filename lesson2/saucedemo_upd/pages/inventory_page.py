from pages.base_page import BasePage
from data import InventoryData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage(BasePage):

    _add_to_cart_button = (By.XPATH, f'//button[@data-test="add-to-cart-sauce-labs-{InventoryData.item}"]')
    _cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
    _remove_from_cart_button = (By.XPATH, f'//button[@data-test="remove-sauce-labs-{InventoryData.item}"]')
    _item_card = (By.ID, f'item_{InventoryData.item_id}_title_link')
    _item_card_image = (By.XPATH, f"//a[@id='item_{InventoryData.item_id}_img_link']/img")
    _shopping_cart_link = (By.CLASS_NAME, 'shopping_cart_link')
    _filter_dd = (By.XPATH, '//select[@data-test="product_sort_container"]')
    _items = (By.CLASS_NAME, 'inventory_item_name ')
    _items_prices = (By.CLASS_NAME, 'inventory_item_price')
    _burger_menu_button = (By.ID, 'react-burger-menu-btn')
    _logout_button = (By.ID, 'logout_sidebar_link')
    _about_button = (By.ID, 'about_sidebar_link')
    _reset_button = (By.ID, 'reset_sidebar_link')

    def add_to_cart(self):
        return self.driver.find_element(*self._add_to_cart_button)
    
    def cart_badge(self):
        return self.driver.find_element(*self._cart_badge)
    
    def remove_from_cart(self):
        return self.driver.find_element(*self._remove_from_cart_button)
    
    def item_card(self):
        return self.driver.find_element(*self._item_card)
    
    def item_card_image(self):
        return self.driver.find_element(*self._item_card_image)
    
    def shopping_cart(self):
        return self.driver.find_element(*self._shopping_cart_link)
    
    def select_filter(self, value):
        filter_dd = self.driver.find_element(*self._filter_dd)
        filter_value = Select(filter_dd)
        return filter_value.select_by_value(value)
    
    def items_sorting(self, option, reverse_state):
        if option == 'price':
            items = self.driver.find_elements(*self._items_prices)
            items_list = [float(item_price.text.strip('$')) for item_price in items]
        elif option == 'abc':
            items = self.driver.find_elements(*self._items)
            items_list = [item.text for item in items]
        return items_list == sorted(items_list, reverse=reverse_state)
    
    def burger_menu(self):
        return self.driver.find_element(*self._burger_menu_button)
    
    def logout(self):
        return self.driver.find_element(*self._logout_button)
    
    def about(self):
        return self.driver.find_element(*self._about_button)
    
    def reset(self):
        return self.driver.find_element(*self._reset_button)
    