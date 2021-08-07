import time
import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
link1 = "http://selenium1py.pythonanywhere.com/"
class TestGuestAndUserAddProductToBasketAndGoToLoginPage:


    def test_user_can_add_product_to_basket(self, browser):
        email = (str(time.time())) + "@fakemail.org"
        password = str((time.time()) +20)
        page = MainPage(browser, link1)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        product = ProductPage(browser, link)
        product.open()
        product.add_to_cart_foo()
        product.item_added_to_cart()
        product.item_added_to_cart_right()


    def test_guest_can_add_product_to_basket(self, browser):
        product = ProductPage(browser, link)
        product.open()
        product.add_to_cart_foo()
        product.item_added_to_cart()
        product.item_added_to_cart_right()


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.url)
        basket_page.should_be_basket_page()

    @pytest.mark.need_review
    def test_guest_can_go_login_link_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.add_to_cart_foo()
        page.item_added_to_cart()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.url)
        login_page.should_be_login_page()

    @pytest.mark.need_review
    def test_guest_can_go_login_link_from_product_page_add_item_to_basket(self, browser):

        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.add_to_cart_foo()
        page.item_added_to_cart()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.url)
        login_page.should_be_login_page()










