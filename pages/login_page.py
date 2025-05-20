import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL


class LoginPage(BasePage):
    """Страница логина NordClan."""

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

    def open(self):
        """Открывает страницу логина."""
        self.driver.get(BASE_URL)

    def login(self, username, password):
        """
        Выполняет вход в систему.

        :param username: Имя пользователя
        :param password: Пароль
        """

        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)
        time.sleep(2)


    def is_login_form_presented(self):
        """
        Проверяет наличие формы логина на странице.

        :return: True, если форма логина отображается
        """
        return self.is_element_present(self.USERNAME) and self.is_element_present(self.PASSWORD)
