from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        self.basket_not_empty()
        self.basket_empty()

    def basket_not_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), "Content is presented, but should not be"

    def basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.CONTENT_INNER), "Massage is not presented"
