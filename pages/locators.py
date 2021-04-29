from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_ITEM = (By.CSS_SELECTOR, "div.product_main h1")
    COST_ITEM = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ALERT_INNER_ITEM = (By.CSS_SELECTOR, "div.alert-success div.alertinner strong")
    ALERT_INNER_COST = (By.CSS_SELECTOR, "div.alert-info div.alertinner strong")
