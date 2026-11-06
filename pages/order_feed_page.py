import allure

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Получаем счётчик выполненных заказов за всё время")
    def get_total_orders_counter(self):
        counter = self.get_element_text(
            OrderFeedLocators.TOTAL_ORDERS_COUNTER
        )
        return int(counter)

    @allure.step("Получаем счётчик выполненных заказов за сегодня")
    def get_today_orders_counter(self):
        counter = self.get_element_text(
            OrderFeedLocators.TODAY_ORDERS_COUNTER
        )
        return int(counter)

    @allure.step("Получаем номера заказов в разделе «В работе»")
    def get_orders_in_progress(self):
        return self.get_elements_text(
            OrderFeedLocators.ORDERS_IN_PROGRESS_NUMBERS
        )

    @allure.step("Ожидаем увеличения счётчика заказов за всё время")
    def wait_for_total_orders_counter(self, initial_counter):
        self.wait_for_condition(
            lambda driver: self.get_total_orders_counter() > initial_counter
        )

    @allure.step("Ожидаем увеличения счётчика заказов за сегодня")
    def wait_for_today_orders_counter(self, initial_counter):
        self.wait_for_condition(
            lambda driver: self.get_today_orders_counter() > initial_counter
        )

    @allure.step("Ожидаем появления созданного заказа в разделе «В работе»")
    def wait_for_order_in_progress(self, order_number):
        # Форматируем номер заказа для отображения в ленте
        order_number = order_number.zfill(5)

        def check_order(driver):
            orders = self.get_orders_in_progress()
            print(f"Ожидаемый номер: {order_number}")
            print(f"Заказы в работе: {orders}")
            return order_number in orders

        self.wait_for_condition(
            check_order,
            timeout=60,
            poll_frequency=0.1
        )