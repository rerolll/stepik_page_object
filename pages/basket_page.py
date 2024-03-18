from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empety(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_EMPETY
        ), "Basket is not empety"

    def should_be_text_basket_is_empety(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPETY_TEXT
        ), "Basket has no text empety work only on en-gb language"
