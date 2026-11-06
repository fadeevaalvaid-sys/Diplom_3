
from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Счётчик выполненных заказов за всё время
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )

    # Счётчик выполненных заказов за сегодня
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )

    # Номера заказов в разделе «В работе»
    ORDERS_IN_PROGRESS_NUMBERS = (
        By.XPATH,
        "//p[text()='В работе:']/following-sibling::ul[contains(@class, 'OrderFeed_orderList__')][1]/li"
    )
