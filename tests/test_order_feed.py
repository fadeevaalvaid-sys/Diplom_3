import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title("Создание заказа и отображение его в ленте заказов")
    def test_create_order(self, logged_in_driver):
        # Создаём объекты страниц
        main_page = MainPage(logged_in_driver)
        order_feed_page = OrderFeedPage(logged_in_driver)

        # Переходим в ленту заказов
        main_page.click_order_feed_link()

        # Запоминаем начальное значение счётчика за всё время
        initial_total_counter = order_feed_page.get_total_orders_counter()

        # Запоминаем начальное значение счётчика за сегодня
        initial_today_counter = order_feed_page.get_today_orders_counter()

        # Возвращаемся в конструктор
        main_page.click_constructor_link()

        # Добавляем ингредиент в конструктор
        main_page.drag_ingredient_to_constructor()

        # Нажимаем кнопку оформления заказа
        main_page.click_order_button()

        # Получаем номер созданного заказа
        order_number = main_page.get_order_number()

        # Закрываем модальное окно с номером заказа
        main_page.close_order_modal()

        # Переходим в ленту заказов
        main_page.click_order_feed_link()

        # Ждём увеличения счётчика заказов за всё время
        order_feed_page.wait_for_total_orders_counter(initial_total_counter)

        # Ждём увеличения счётчика заказов за сегодня
        order_feed_page.wait_for_today_orders_counter(initial_today_counter)

        # Проверяем увеличение счётчика заказов за всё время
        assert order_feed_page.get_total_orders_counter() > initial_total_counter

        # Проверяем увеличение счётчика заказов за сегодня
        assert order_feed_page.get_today_orders_counter() > initial_today_counter

        # Ждём появления созданного заказа в разделе «В работе»
        order_feed_page.wait_for_order_in_progress(order_number)

        # Проверяем, что номер созданного заказа появился в разделе «В работе»
        assert order_number.zfill(5) in order_feed_page.get_orders_in_progress()