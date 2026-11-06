
import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу")
    def open_page(self, url):
        # Открываем страницу по указанному URL
        self.driver.get(url)

    @allure.step("Ожидаем появления видимого элемента")
    def find_visible_element(self, locator, timeout=10):
        # Ожидаем появления видимого элемента
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидаем, когда элемент станет кликабельным")
    def find_clickable_element(self, locator, timeout=10):
        # Ожидаем кликабельности элемента
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Нажимаем на элемент")
    def click_element(self, locator, timeout=10):
        # Находим кликабельный элемент и нажимаем на него
        self.find_clickable_element(locator, timeout).click()

    @allure.step("Нажимаем на элемент через JavaScript")
    def click_element_with_js(self, locator, timeout=10):
        # Находим элемент на странице
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

        # Нажимаем на элемент через JavaScript
        self.driver.execute_script(
            "arguments[0].click();", element
        )

    @allure.step("Получаем текст элемента")
    def get_element_text(self, locator, timeout=10):
        # Получаем текст видимого элемента
        element = self.find_visible_element(locator, timeout)
        return element.text

    @allure.step("Получаем текст нескольких элементов")
    def get_elements_text(self, locator, timeout=10):
        # Ожидаем появления видимых элементов
        elements = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
        return [element.text for element in elements]

    @allure.step("Ожидаем исчезновения элемента")
    def wait_until_invisible(self, locator, timeout=10):
        # Ожидаем исчезновения элемента
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Ожидаем перехода по URL")
    def wait_for_url(self, url, timeout=10):
        # Ожидаем перехода на указанный URL
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        # Получаем адрес текущей страницы
        return self.driver.current_url

    @allure.step("Проверяем отображение элемента")
    def is_element_displayed(self, locator):
        # Проверяем, что элемент отображается
        return self.find_visible_element(locator).is_displayed()

    @allure.step("Ожидаем выполнения условия")
    def wait_for_condition(self, condition, timeout=30, poll_frequency=0.5):
        WebDriverWait(
            self.driver,
            timeout,
            poll_frequency=poll_frequency
        ).until(condition)

    @allure.step("Перетаскиваем элемент с помощью HTML5-событий")
    def drag_and_drop_html5(self, source_locator, target_locator):
        # Находим элемент, который нужно перетащить
        source = self.find_visible_element(source_locator)

        # Находим область, в которую нужно перетащить элемент
        target = self.find_visible_element(target_locator)

        # Выполняем HTML5-перетаскивание через события JavaScript
        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
        """, source, target)
