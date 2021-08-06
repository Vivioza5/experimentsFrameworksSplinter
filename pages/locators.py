from selenium.webdriver.common.by import By

class MainLocators():
    LINK= "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (".icon-user")
    LOGIN_LINK_SPLINTER = ("#login_link")
# разобраться как в сплинтер передавать кортежи

class BasketPageLocators():
    BASKET_PAGE=(By.CSS_SELECTOR, "#basket")
    BASKET_ITEM=(By.CLASS_NAME, "basket-items")
    BASKET_EMPTY_MESS=(By.ID, "content_inner")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET_BTN = ("div.basket-mini.pull-right.hidden-xs a")


class LoginPageLocators():
    LOGIN_FORM = ("#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_EMAIL= (By.NAME, "registration-email")
    PASSWORD_INPUT = (By.NAME, "registration-password1")
    PASSWORD_CONFIRM_INPUT=(By.NAME,"registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_BASKET_BTN = ("#add_to_basket_form")
    PRODUCT_NAME = (".col-sm-6.product_main h1")
    PRODUCT_PRICE = (".price_color")
    PRODUCT_BASKET_MESSAGE = ("//*[@id='messages']")
    PRODUCT_BASKET_MESSAGE_NAME = ("//*[@id='messages']/div[1]/div")


