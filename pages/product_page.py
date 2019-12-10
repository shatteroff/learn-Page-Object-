from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_same_product_in_basket(self):
        self.should_be_name_of_product()
        self.should_be_price_of_product()

    def should_be_name_of_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        assert product_name == product_basket_name, "Product name in the basket and added are not the same"

    def should_be_price_of_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET).text
        assert product_price == product_basket_price, "Product price in the basket and added are not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
