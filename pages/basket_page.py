from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text.find(
            'Your basket is empty') != -1, 'Basket is not empty'

    def should_not_be_product_summary(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY_FORM), \
            "Product summary is presented, but should not be"
