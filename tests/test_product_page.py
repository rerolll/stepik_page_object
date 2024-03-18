import pytest
import time

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


class TestGuestAddToBasketFromProductPage:
    LINK = (
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )

    @pytest.mark.parametrize(
        "promo",
        [
            0, 1, 2, 3, 4, 5, 6,
            pytest.param(
                7, marks=pytest.mark.xfail(reason="fixing this bug right now")
            ),
            8, 9,
        ],
    )
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, promo):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
        page = ProductPage(browser, link, 0)
        page.open()
        page.should_be_button_add_to_basket()
        page.click_button_add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_added_book_name_message()
        page.should_be_added_book_name_is_correct()
        page.should_be_added_book_price_message()
        page.should_be_added_book_price_is_correct()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(
        self, browser
    ):
        page = ProductPage(browser, self.LINK, 0)
        page.open()
        page.should_be_button_add_to_basket()
        page.click_button_add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.LINK, 0)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.LINK, 0)
        page.open()
        page.should_be_button_add_to_basket()
        page.click_button_add_to_basket()
        page.should_dissapear_of_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, self.LINK)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.LINK, 0)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(
        self, browser
    ):
        page = BasketPage(browser, self.LINK)
        page.open()
        page.go_to_basket_page()
        page.should_be_basket_is_empety()
        page.should_be_text_basket_is_empety()


class TestUserAddToBasketFromProductPage:
    LINK = (
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, self.LINK)
        page.open()
        page.go_to_login_page()
        page.register_new_user(
            email=str(time.time()) + "@fakemail.org", password="Psad1wsadSa"
        )
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.LINK)
        page.open()
        page.should_be_button_add_to_basket()
        page.click_button_add_to_basket()
        page.should_be_added_book_name_message()
        page.should_be_added_book_name_is_correct()
        page.should_be_added_book_price_message()
        page.should_be_added_book_price_is_correct()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.LINK)
        page.open()
        page.should_not_be_success_message()
