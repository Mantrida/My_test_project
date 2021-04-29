
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_button_add_to_basket()  # выполняем метод страницы — переходим на страницу логина
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.verfication_correct_adding()
    time.sleep(30)

