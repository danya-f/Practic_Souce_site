from selenium.webdriver.common.by import By
from time import sleep
from lesson1.help_files.auth_info import *
from lesson1.help_files.selectors import *




def test_login_form(driver):
    driver.get(MAIN_PAGE)
    assert driver.current_url == MAIN_PAGE

    driver.find_element(By.CSS_SELECTOR , USER_NAME).send_keys(standart_login)

    driver.find_element(By.CSS_SELECTOR, PASSWORD).send_keys(password)

    driver.find_element(By.CSS_SELECTOR , LOGIN_BUTTON ).click()

    sleep(2)

    assert driver.current_url == URL_AFTER_LOGIN


def test_login_form_incorrect_log_pass(driver):

    driver.get(MAIN_PAGE)
    assert driver.current_url == MAIN_PAGE

    driver.find_element(By.CSS_SELECTOR , USER_NAME).send_keys('user12')

    driver.find_element(By.CSS_SELECTOR, PASSWORD).send_keys('user')

    driver.find_element(By.CSS_SELECTOR , LOGIN_BUTTON ).click()

    sleep(2)

    assert driver.current_url != URL_AFTER_LOGIN
