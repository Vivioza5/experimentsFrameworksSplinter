import time

import pytest
from selenium import webdriver
from splinter import Browser
link = "http://selenium1py.pythonanywhere.com/"

from .locators import BasePageLocators
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = Browser('chrome')
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
from selenium.webdriver.common.by import By
from pypom import Page
from splinter import Browser
class TestMainPage1():
    # LOGIN_LINK = ('id', "#login_link")
    # LOGIN_LINK = ("#login_link")
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.visit(link)
        browser.find_by_css("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.visit(link)
        time.sleep(10)

