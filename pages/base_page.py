from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from selenium.common.exceptions import NoAlertPresentException
import math
from splinter import Browser
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators, MainPageLocators
from pypom import splinter_driver

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        self.browser.find_by_css(BasePageLocators.LOGIN_LINK).click()


    def go_to_basket_page(self):
        self.browser.find_by_css(MainPageLocators.OPEN_BASKET_BTN).click()
        print(self.browser.url)



    def open(self):
        self.browser.visit(self.url)


    def solve_quiz_and_get_code(self):
        alert=self.browser.get_alert()
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        #если нужен установил таймаут
        # time.sleep(5)
        try:
            alert = self.browser.get_alert()

            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_link(self):
        assert self.browser.is_element_present_by_css(BasePageLocators.LOGIN_LINK), "Login link is not presented"
        print("it is login link")
        # time.sleep(30)m

    def should_be_authorized_user(self):
        assert self.browser.is_element_present_by_css(BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
        print("\nUser was registered")
    # def is_disappeared(self, how, what, timeout=4):
    #
    #     try:
    #         WebDriverWait(self.browser, timeout, 1, TimeoutException). \
    #             until_not(EC.presence_of_element_located((how, what)))
    #     except TimeoutException:
    #         return False
    #
    #     return True