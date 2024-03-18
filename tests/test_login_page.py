from pages.main_page import MainPage


def test_guest_can_go_to_login_page(
    browser, link="https://selenium1py.pythonanywhere.com/accounts/login/"
):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
