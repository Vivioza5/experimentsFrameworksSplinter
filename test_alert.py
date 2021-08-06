import time
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
link = "http://suninjuly.github.io/redirect_accept.html"
link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
class TestAlert():
   def test_guest_should_see_login_link(self, browser):
       page = ProductPage(browser, link1)
       page.open()
       page.should_be_login_link()
       page.add_to_cart_foo()
       page.solve_quiz_and_get_code()




        #
        # print(alert.text)
        # answer = str(math.log(abs((12 * math.sin(float(x))))))
        # alert.send_keys(answer)
        # alert.accept()
        #если нужен установил таймаут
        # time.sleep(5)
        # try:
        #     alert = self.browser.get_alert()
        #     alert_text = alert.text
        #     print(f"Your code: {alert_text}")
        #     alert.accept()
        # except NoAlertPresentException:
        #     print("No second alert presented")
