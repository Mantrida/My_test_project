
from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):


    def should_be_button_add_to_basket(self):
        # реализуйте проверку, что есть кнопка добавления в корзину
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button is not presented"

    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_basket.click()

    def verfication_correct_adding(self):
        item_name = self.browser.find_element(*ProductPageLocators.NAME_ITEM).text
        alertinner_item = self.browser.find_element(*ProductPageLocators.ALERT_INNER_ITEM).text
        assert item_name == alertinner_item, "Item name is not correct"

        cost_item = self.browser.find_element(*ProductPageLocators.COST_ITEM).text
        alertinner_cost = self.browser.find_element(*ProductPageLocators.ALERT_INNER_COST).text
        assert cost_item == alertinner_cost, "Cost item is not correct"

