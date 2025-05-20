import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    finder = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    first_element = browser.find_element(By.LINK_TEXT, finder)
    first_element.click()

    first_name_input = browser.find_element(By.NAME, "first_name")
    first_name_input.send_keys('Mike')

    last_name_input = browser.find_element(By.NAME, "last_name")
    last_name_input.send_keys('Kar')

    city = browser.find_element(By.CLASS_NAME, "city")
    city.send_keys('San Francisco')

    country = browser.find_element(By.ID, "country")
    country.send_keys('US')

    submit = browser.find_element(By.CLASS_NAME, "btn btn-default")
    submit.click()
finally:
    time.sleep(30)
    browser.quit()
