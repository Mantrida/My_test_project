
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):


    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button is not presented"

    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_basket.click()

    def verfication_correct_item(self, item_name):
        alertinner_item = self.browser.find_element(*ProductPageLocators.ALERT_INNER_ITEM).text
        assert item_name == alertinner_item, "Item name is not correct"

    def verfication_correct_cost(self, cost_item):
        alertinner_cost = self.browser.find_element(*ProductPageLocators.ALERT_INNER_COST).text
        assert cost_item == alertinner_cost, "Cost item is not correct"

    def verfication_correct_adding(self):
        item_name = self.browser.find_element(*ProductPageLocators.NAME_ITEM).text
        self.verfication_correct_item(item_name)

        cost_item = self.browser.find_element(*ProductPageLocators.COST_ITEM).text
        self.verfication_correct_cost(cost_item)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_INNER_ITEM), \
           "Success message is presented, but should not be"

    def should_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_INNER_ITEM), \
            "Success message is not disappeared"
