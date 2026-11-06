
import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import BASE_URL


class LoginPage(BasePage):

    @allure.step("Вводим электронную почту")
    def enter_email(self, email):
        # Вводим электронную почту
        self.find_visible_element(
            LoginPageLocators.EMAIL_INPUT
        ).send_keys(email)

    @allure.step("Вводим пароль")
    def enter_password(self, password):
        # Вводим пароль
        self.find_visible_element(
            LoginPageLocators.PASSWORD_INPUT
        ).send_keys(password)

    @allure.step("Нажимаем кнопку входа")
    def click_login_button(self):
        # Нажимаем кнопку входа
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Ожидаем успешной авторизации")
    def wait_for_login(self):
        # Ожидаем перехода на главную страницу
        self.wait_for_url(BASE_URL)

    @allure.step("Авторизуемся на сайте")
    def login(self, email, password):
        # Вводим данные и выполняем вход
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_login()
