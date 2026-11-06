import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Переходим в конструктор")
    def click_constructor_link(self):
        # Нажимаем на ссылку конструктора
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step("Переходим в ленту заказов")
    def click_order_feed_link(self):
        # Нажимаем на ссылку ленты заказов
        self.click_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Открываем модальное окно деталей ингредиента")
    def open_ingredient_modal(self):
        # Нажимаем на первый ингредиент
        self.click_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Проверяем отображение модального окна ингредиента")
    def is_ingredient_modal_displayed(self):
        # Проверяем отображение заголовка модального окна
        return self.is_element_displayed(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        )

    @allure.step("Закрываем модальное окно ингредиента")
    def close_ingredient_modal(self):
        # Нажимаем на крестик модального окна
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Проверяем закрытие модального окна ингредиента")
    def is_ingredient_modal_closed(self):
        # Проверяем, что заголовок модального окна исчез
        return self.wait_until_invisible(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        )

    @allure.step("Получаем счётчик ингредиента")
    def get_ingredient_counter(self):
        # Получаем значение счётчика ингредиента
        counter = self.get_element_text(
            MainPageLocators.INGREDIENT_COUNTER
        )
        return int(counter)

    @allure.step("Добавляем ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        # Перетаскиваем первый ингредиент в область конструктора
        self.drag_and_drop_html5(
            MainPageLocators.FIRST_INGREDIENT,
            MainPageLocators.CONSTRUCTOR_DROP_ZONE
        )

    @allure.step("Нажимаем кнопку оформления заказа")
    def click_order_button(self):
        # Нажимаем кнопку оформления заказа
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Получаем номер созданного заказа")
    def get_order_number(self):
        # Ждём, пока временный номер 9999 заменится настоящим
        def is_order_number_ready(driver):
            order_number = self.find_visible_element(
                MainPageLocators.ORDER_NUMBER
            ).get_attribute("textContent").strip()

            return order_number.isdigit() and order_number != "9999"

        self.wait_for_condition(
            is_order_number_ready,
            timeout=30
        )

        # Получаем настоящий номер заказа
        order_number = self.find_visible_element(
            MainPageLocators.ORDER_NUMBER
        ).get_attribute("textContent").strip()

        # Приводим номер к формату из пяти цифр
        return order_number.zfill(5)

    @allure.step("Закрываем модальное окно созданного заказа")
    def close_order_modal(self):
        # Ждём появления номера заказа
        self.find_visible_element(
            MainPageLocators.ORDER_NUMBER
        )

        # Нажимаем на крестик через JavaScript
        self.click_element_with_js(
            MainPageLocators.CLOSE_MODAL_BUTTON
        )

        # Ждём закрытия модального окна
        self.wait_until_invisible(
            MainPageLocators.ORDER_NUMBER
        )