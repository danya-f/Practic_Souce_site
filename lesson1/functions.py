from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from auth_info import *
from CSS_selectors import *


def log_in(driver):
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.CSS_SELECTOR, ID_USER_NAME)
    username_field.send_keys(standart_login)

    password_field = driver.find_element(By.CSS_SELECTOR, ID_PASSWORD)
    password_field.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, ID_LOGIN_BUTTON)
    login_button.click()

    sleep(1)

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'


def add_2_item(driver):
    log_in(driver)
    add_item_button_1 = driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_1)
    add_item_button_1.click()
    sleep(1)
    a = driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART)
    add_item_button_2 = driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_2)
    add_item_button_2.click()
    sleep(1)
    assert a.text == '2'