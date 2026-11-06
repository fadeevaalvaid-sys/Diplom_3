
import os
import shutil

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from pages.login_page import LoginPage
from urls import BASE_URL

load_dotenv()


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        chromedriver_path = shutil.which("chromedriver")
        browser = webdriver.Chrome(
            service=ChromeService(executable_path=chromedriver_path)
        )

    elif request.param == "firefox":
        geckodriver_path = shutil.which("geckodriver")
        browser = webdriver.Firefox(
            service=FirefoxService(executable_path=geckodriver_path)
        )

    yield browser
    browser.quit()


@pytest.fixture
def logged_in_driver(driver):
    # Получаем учётные данные из переменных окружения
    email = os.getenv("STELLAR_EMAIL")
    password = os.getenv("STELLAR_PASSWORD")

    # Проверяем наличие учётных данных
    assert email is not None
    assert password is not None

    # Создаём объект страницы авторизации
    login_page = LoginPage(driver)

    # Открываем страницу авторизации
    login_page.open_page(BASE_URL + "login")

    # Выполняем авторизацию
    login_page.login(email, password)

    return driver
