import pytest
from selenium import webdriver

from utils.config import VALID_USERNAME, VALID_PASSWORD, HEADLESS
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage


def __create_chrome_options():
    """Задает режим запуска Хрома."""

    options = webdriver.ChromeOptions()

    if HEADLESS:
        options.add_argument('--headless')

    return options


@pytest.fixture(scope="module")
def driver():
    """
    Фикстура, создающая один экземпляр браузера на весь модуль.

    :return: Драйвер Selenium
    """

    options = __create_chrome_options()
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(3)

    yield driver

    driver.quit()


@pytest.fixture(scope="module")
def login_page(driver):
    """
    Возвращает инициализированный объект LoginPage.
    Страница будет открыта через метод open(), чтобы избежать дублирования логики.

    :param driver: Экземпляр драйвера Selenium
    :return: Объект LoginPage
    """
    page = LoginPage(driver)
    page.open()
    return page


@pytest.fixture(scope="module")
def logged_in_project_page(login_page):
    """
    Выполняет вход в систему и возвращает объект ProjectsPage.

    :param login_page: Объект LoginPage
    :return: Объект ProjectsPage
    """
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return ProjectsPage(login_page.driver)
