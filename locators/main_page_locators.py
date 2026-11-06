
from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']")
    ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed']")

    FIRST_INGREDIENT = (
        By.XPATH,
        "//a[contains(@class, 'BurgerIngredient_ingredient')]"
    )

    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//*[normalize-space()='Детали ингредиента']"
    )

    CLOSE_MODAL_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//button[.//*[name()='path']]"
    )

    INGREDIENT_COUNTER = (
        By.CSS_SELECTOR,
        "p[class*='counter_counter__num']"
    )

    CONSTRUCTOR_DROP_ZONE = (
        By.CSS_SELECTOR,
        "ul[class*='BurgerConstructor_basket__list']"
    )

    # Кнопка оформления заказа
    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )

    # Номер созданного заказа в модальном окне
    ORDER_NUMBER = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__contentBox')]//h2"
    )
