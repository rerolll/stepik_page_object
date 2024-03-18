from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Не корректный url адрес"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_EMAIL
        ), "E-mail input is not presented on login form"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_PW
        ), "Password input is not presented on login form"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_BTN
        ), "Submit button is not presented on login form"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "REGISTER form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(
            email
        )
        self.browser.find_element(*LoginPageLocators.REGISTER_PW1).send_keys(
            password
        )
        self.browser.find_element(*LoginPageLocators.REGISTER_PW2).send_keys(
            password
        )
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_ALERT_SUCCESS
        ), "Couldn't register"
