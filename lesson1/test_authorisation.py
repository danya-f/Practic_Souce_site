from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from auth_info import *
from CSS_selectors import *



def test_login_form():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.CSS_SELECTOR , ID_USER_NAME)
    username_field.send_keys(standart_login)

    password_field = driver.find_element(By.CSS_SELECTOR, ID_PASSWORD)
    password_field.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR , ID_LOGIN_BUTTON )
    login_button.click()

    sleep(5)

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    driver.close()


def test_login_form_uncorrect_log_pass():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.CSS_SELECTOR , ID_USER_NAME)
    username_field.send_keys('user')

    password_field = driver.find_element(By.CSS_SELECTOR, ID_PASSWORD)
    password_field.send_keys('user')

    login_button = driver.find_element(By.CSS_SELECTOR , ID_LOGIN_BUTTON )
    login_button.click()

    sleep(5)

    assert driver.current_url != 'https://www.saucedemo.com/inventory.html'
    driver.quit()
