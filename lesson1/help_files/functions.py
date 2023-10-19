from selenium.webdriver.common.by import By
from time import sleep
from lesson1.help_files.auth_info import *
from lesson1.help_files.CSS_selectors import *
from faker import Faker


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


def login_and_add_2_item(driver):
    log_in(driver)
    add_item_button_1 = driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_1)
    add_item_button_1.click()
    sleep(1)
    a = driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART)
    add_item_button_2 = driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_2)
    add_item_button_2.click()
    sleep(1)
    assert a.text == '2'

def go_to_cart(driver):
    icon_cart = driver.find_element(By.XPATH , XPATH_SHOPPING_CART)
    icon_cart.click()

def push_checkout(driver):
    icon_checkout = driver.find_element(By.XPATH , XPATH_CHECKOUT_BUTTON_ON_CART)
    icon_checkout.click()

def enter_info_checkout_step_1(driver):
    firstname_field = driver.find_element(By.XPATH , XPATH_ENTER_FIRSTNAME)
    lastname_field = driver.find_element(By.XPATH , XPATH_ENTER_LASTNAME)
    zipcode_field = driver.find_element(By.XPATH , XPATH_ENTER_ZIPCODE)
    firstname_field.send_keys(firstname)
    lastname_field.send_keys(lastname)
    zipcode_field.send_keys(zipcode)

def push_continue_on_checkout(driver):
    confirm = driver.find_element(By.XPATH , XPATH_CONTINUE_BUTTON)
    confirm.click()

def push_finish_on_checkout(driver):
    finish = driver.find_element(By.XPATH , XPATH_FINISH_BUTTON_ON_CHECKOUT)
    finish.click()
