from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    language_message = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en-gb": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty.",
    }

    def should_be_empty_basket_and_message_empty_basket(self):
        self.should_be_no_items_in_basket()
        self.should_be_message_empty_basket()

    def should_be_no_items_in_basket(self):
        is_empty = self.is_not_element_present(*BasketPageLocators.CONTENTS_OF_BASKET)
        assert is_empty, "The basket is not empty"

    def should_be_message_empty_basket(self):
        text_message = self.get_text_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET)
        language_page = self.get_current_language()
        expected_message = self.language_message.get(language_page, "en-gb")
        assert expected_message in text_message, "There is no message that the basket is empty"
