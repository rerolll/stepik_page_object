import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage

from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASCKET
        ), "Login link is not presented"

    def click_button_add_to_basket(self):
        self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASCKET
        ).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_added_book_name_message(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ADD_PRODUCT
        ), "Нет сообщения об успешном добавления товара в корзину"

    def should_be_added_book_name_is_correct(self):
        added_message = self.browser.find_element(
            *ProductPageLocators.MESSAGE_ADD_PRODUCT
        )
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        )
        assert (
            product_name.text == added_message.text
        ), "Название продукта не соответсвует добавленному в корзину"

    def should_be_added_book_price_message(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ADD_PRODUCT_PRICE
        ), "Нет сообщения со стоимостью корзины"

    def should_be_added_book_price_is_correct(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        )
        added_product_price = self.browser.find_element(
            *ProductPageLocators.MESSAGE_ADD_PRODUCT_PRICE
        )
        assert (
            product_price.text in added_product_price.text
        ), "Цена добавленного продукта не соответствует цене выбранного продукта"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.MESSAGE_ADD_PRODUCT
        ), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.MESSAGE_ADD_PRODUCT
        ), "Success message is presented, but should is disappeared"
