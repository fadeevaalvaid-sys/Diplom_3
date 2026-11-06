
import allure

from pages.main_page import MainPage
from urls import BASE_URL


@allure.title("Переход в ленту заказов")
def test_go_to_order_feed(driver):
    # Создаём объект главной страницы
    main_page = MainPage(driver)

    # Открываем главную страницу
    main_page.open_page(BASE_URL)

    # Переходим в ленту заказов
    main_page.click_order_feed_link()

    # Проверяем, что открылась лента заказов
    assert main_page.get_current_url() == BASE_URL + "feed"


@allure.title("Переход в конструктор")
def test_go_to_constructor(driver):
    # Создаём объект главной страницы
    main_page = MainPage(driver)

    # Открываем ленту заказов
    main_page.open_page(BASE_URL + "feed")

    # Переходим в конструктор
    main_page.click_constructor_link()

    # Проверяем, что открылся конструктор
    assert main_page.get_current_url() == BASE_URL


@allure.title("Открытие модального окна деталей ингредиента")
def test_open_ingredient_modal(driver):
    # Создаём объект главной страницы
    main_page = MainPage(driver)

    # Открываем главную страницу
    main_page.open_page(BASE_URL)

    # Открываем модальное окно с деталями ингредиента
    main_page.open_ingredient_modal()

    # Проверяем, что модальное окно отображается
    assert main_page.is_ingredient_modal_displayed()


@allure.title("Закрытие модального окна деталей ингредиента")
def test_close_ingredient_modal(driver):
    # Создаём объект главной страницы
    main_page = MainPage(driver)

    # Открываем главную страницу
    main_page.open_page(BASE_URL)

    # Открываем модальное окно с деталями ингредиента
    main_page.open_ingredient_modal()

    # Закрываем модальное окно нажатием на крестик
    main_page.close_ingredient_modal()

    # Проверяем, что модальное окно закрылось
    assert main_page.is_ingredient_modal_closed()


@allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
def test_drag_ingredient_to_constructor(logged_in_driver):
    # Создаём объект главной страницы
    main_page = MainPage(logged_in_driver)

    # Получаем начальное значение счётчика ингредиента
    initial_counter = main_page.get_ingredient_counter()

    # Перетаскиваем ингредиент в конструктор
    main_page.drag_ingredient_to_constructor()

    # Проверяем, что счётчик ингредиента увеличился
    assert main_page.get_ingredient_counter() > initial_counter
