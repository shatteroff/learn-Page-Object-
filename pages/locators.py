from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]/*//a')

# class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    PRODUCT_NAME_BASKET = (By.XPATH, '//div[@class="alertinner "]/strong')
    PRODUCT_PRICE_BASKET = (By.XPATH, '*//div[@class="alert alert-safe alert-noicon alert-info  fade in"]/*//strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner ")


class BasketPageLocators():
    EMPTY_BASKET = (By.XPATH, "//div[@id='content_inner']/p")
    BASKET_SUMMARY_FORM = (By.CLASS_NAME, 'basket_summary')