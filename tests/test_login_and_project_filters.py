import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import BASE_URL


# Тест 1: Открытие страницы логина
def test_open_login_page(login_page):
    """Проверяет, что форма логина открыта и доступна."""
    assert login_page.is_login_form_presented(), "Форма логина не найдена"


# Тест 2: Ввод неправильного логина и пароля
def test_login_with_invalid_credentials(login_page, driver):
    """
    Проверяет, что при вводе неверных учетных данных отображается
    сообщение 'Неверный логин/пароль. Проверьте данные'.
    """

    invalid_username = "invalid_user"
    invalid_password = "wrong_password"
    login_page.login(invalid_username, invalid_password)

    error_message_locator = (By.XPATH, "//div[text()='Неверный логин/пароль. Проверьте данные']")

    assert login_page.is_element_present(error_message_locator), \
        "Сообщение об ошибке не отображается при неверных данных"

    assert driver.current_url == BASE_URL, \
        "URL изменился — возможно, вход выполнен с неверными данными"


# Тест 3: Вход с корректными данными
def test_login_with_valid_credentials(logged_in_project_page):
    """Проверяет, что пользователь может войти с корректными учетными данными."""

    assert logged_in_project_page.is_at_projects_page(), "Не удалось войти в систему с корректными данными"


# Тест 4: Проверка заголовка на странице "Мои проекты"
def test_check_header_on_projects_page(logged_in_project_page):
    """Проверяет, что на странице 'Мои проекты' отображается корректный заголовок."""
    expected_headers = ["My Projects", "Мои проекты"]

    header_text = logged_in_project_page.get_projects_page_header_text()
    assert header_text in expected_headers, f"Ожидался заголовок '{expected_headers[0]}' или '{expected_headers[1]}', получено: '{header_text}'"


# Тест 5: Выбор типа проекта
def test_select_internal_project_type(driver, logged_in_project_page):
    """
    Проверяет, что можно выбрать тип проекта 'Внутренний' (или 'Internal'),
    из выпадающего списка и убедиться, что он выбран.
    """

    PROJECT_TYPE_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, ".Select-control")
    OPTION_INTERNAL_LOCATOR = (
        By.XPATH, "//div[@class='Select-menu']//div[normalize-space()='Внутренний' or normalize-space()='Internal']")
    SELECTED_VALUE_LOCATOR = (By.CSS_SELECTOR, ".Select-value-label")

    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PROJECT_TYPE_DROPDOWN_LOCATOR)
    )
    dropdown.click()

    time.sleep(1)

    option = WebDriverWait(logged_in_project_page.driver, 10).until(
        EC.element_to_be_clickable(OPTION_INTERNAL_LOCATOR)
    )
    option.click()

    selected_value = WebDriverWait(logged_in_project_page.driver, 10).until(
        EC.visibility_of_element_located(SELECTED_VALUE_LOCATOR)
    )

    assert selected_value.text.strip() in ["Внутренний", "Internal"], \
        f"Ожидалось 'Внутренний' или 'Internal', получено '{selected_value.text}'"


# Тест 6: Ввод названия проекта
def test_enter_project_name(logged_in_project_page, driver):
    """
    Проверяет, что можно ввести название проекта в соответствующее поле
    и убедиться, что оно отображается корректно.
    """

    PROJECT_NAME_INPUT_LOCATOR = (
        By.XPATH,
        "//input[normalize-space(@placeholder)='Enter the project name' or normalize-space(@placeholder)='Введите название проекта']"
    )

    project_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PROJECT_NAME_INPUT_LOCATOR)
    )
    project_name_input.clear()

    project_name_input.send_keys("Привет")

    entered_value = project_name_input.get_attribute("value")

    time.sleep(3)

    assert entered_value == "Привет", \
        f"Ожидалось значение 'Привет', получено '{entered_value}'"
