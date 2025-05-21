from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProjectsPage(BasePage):
    """Страница 'Мои проекты'."""

    HEADER_LOCATOR = (By.CSS_SELECTOR, "header h1")

    def is_at_projects_page(self):
        """
        Проверяет, что текущая страница — 'Мои проекты'.

        :return: True, если заголовок совпадает
        """
        return self.is_element_present(self.HEADER_LOCATOR)

    def get_projects_page_header_text(self):
        """Возвращает текст заголовка на странице 'Мои проекты'."""

        return self.get_text(self.HEADER_LOCATOR)
