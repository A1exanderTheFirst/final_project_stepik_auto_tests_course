from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".page_inner .basket-mini a.btn.btn-default")
    CURRENT_LANGUAGE = (By.CSS_SELECTOR, "#language_selector [name='language'] > [selected]")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form",)
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > .alertinner > strong")
    MESSAGE_CART_COST = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner > p:nth-child(1) > strong")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    CONTENTS_OF_BASKET = (By.CSS_SELECTOR, "#content_inner > #basket_formset")
