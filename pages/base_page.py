from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Базовый класс для всех страниц. Содержит общие методы взаимодействия с элементами."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_element(self, locator):
        """
        Нажимает на элемент, найденный по локатору.

        :param locator: Локатор элемента (кортеж, например, (By.ID, 'id_example'))
        """
        element = self.driver.find_element(*locator)
        element.click()

    def type_text(self, locator, text):
        """
        Вводит текст в поле, найденное по локатору.

        :param locator: Локатор поля ввода
        :param text: Текст для ввода
        """
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Получает текст элемента.

        :param locator: Локатор элемента
        :return: Текст элемента
        """
        return self.driver.find_element(*locator).text

    def is_element_present(self, locator):
        """
        Проверяет, присутствует ли элемент на странице.

        :param locator: Локатор элемента
        :return: True, если элемент найден, иначе False
        """
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def select_dropdown_by_visible_text(self, locator, text):
        """
        Выбирает опцию из выпадающего списка по видимому тексту.

        :param locator: Локатор выпадающего списка
        :param text: Текст опции
        """
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(text)

    def get_selected_dropdown_text(self, locator):
        """
        Получает текст выбранной опции из выпадающего списка.

        :param locator: Локатор выпадающего списка
        :return: Текст выбранной опции
        """
        select = Select(self.driver.find_element(*locator))
        return select.first_selected_option.text

    def get_input_value(self, locator):
        """
        Получает значение атрибута value у поля ввода.

        :param locator: Локатор поля ввода
        :return: Значение атрибута value
        """
        return self.driver.find_element(*locator).get_attribute("value")
