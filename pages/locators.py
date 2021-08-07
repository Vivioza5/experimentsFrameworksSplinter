from selenium.webdriver.common.by import By

class MainLocators():
    LINK= "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class BasePageLocators():
    LOGIN_LINK = ("#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (".icon-user")

# разобраться как в сплинтер передавать кортежи

class BasketPageLocators():
    BASKET_PAGE=( "#basket")
    BASKET_ITEM=(".basket-items")
    BASKET_EMPTY_MESS=("#content_inner")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET_BTN = ("div.basket-mini.pull-right.hidden-xs a")


class LoginPageLocators():
    LOGIN_FORM = ("#login_form")
    REGISTER_FORM = ("#register_form")
    LOGIN_EMAIL= ("registration-email")
    PASSWORD_INPUT = ( "registration-password1")
    PASSWORD_CONFIRM_INPUT=("registration-password2")
    REGISTER_BUTTON = ("registration_submit")


class ProductPageLocators():
    ADD_BASKET_BTN = ("#add_to_basket_form")
    PRODUCT_NAME = (".col-sm-6.product_main h1")
    PRODUCT_PRICE = (".price_color")
    PRODUCT_BASKET_MESSAGE = ("//*[@id='messages']")
    PRODUCT_BASKET_MESSAGE_NAME = ("//*[@id='messages']/div[1]/div")


