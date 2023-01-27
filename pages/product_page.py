from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_the_add_to_cart_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "product name not found"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "product price not found"

    def should_be_message_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_CART), \
            "there is no message about adding an item to the basket"

    def should_be_message_basket_cost(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_CART_COST), \
            "there is no message about the cost of the basket"

    def should_be_equal_product_names(self):
        product_name = self.get_text_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_message = self.get_text_element(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_CART)
        assert product_name == product_name_in_message, f"the product names don't match: " \
                                                        f"'{product_name}' != '{product_name_in_message}'"

    def get_text_element(self, how, what):
        return self.browser.find_element(how, what).text

    def should_be_same_price_of_product_and_basket(self):
        product_price = self.get_text_element(*ProductPageLocators.PRODUCT_PRICE)
        message_product_price = self.get_text_element(*ProductPageLocators.MESSAGE_CART_COST)
        assert product_price == message_product_price, \
            f"prices don't match: '{product_price}' != '{message_product_price}'"

    def should_be_after_successfully_adding_to_basket(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_message_product_added_to_basket()
        self.should_be_message_basket_cost()

        self.should_be_equal_product_names()
        self.should_be_same_price_of_product_and_basket()
