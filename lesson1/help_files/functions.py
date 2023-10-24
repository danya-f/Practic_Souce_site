from selenium.webdriver.common.by import By
from time import sleep
from lesson1.help_files.auth_info import *
from lesson1.help_files.selectors import *


def log_in(driver):
    driver.get(MAIN_PAGE)

    username_field = driver.find_element(By.CSS_SELECTOR, USER_NAME)
    username_field.send_keys(standart_login)

    password_field = driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password_field.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON)
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

def push_filter_A_Z(driver):
    filtr = driver.find_element(By.XPATH , XPATH_FILTER_BUTTON)
    filtr.click()
    filtr_az = driver.find_element(By.XPATH , FILTER_AZ)
    filtr_az.click()
def push_filter_Z_A(driver):
    filtr = driver.find_element(By.XPATH , XPATH_FILTER_BUTTON)
    filtr.click()
    filtr_za = driver.find_element(By.XPATH , FILTER_ZA)
    filtr_za.click()


def push_filter_low_high(driver):
    filtr = driver.find_element(By.XPATH , XPATH_FILTER_BUTTON)
    filtr.click()
    filtr_lh = driver.find_element(By.XPATH , FILTER_LOW_HIGH)
    filtr_lh.click()


def push_filter_high_low(driver):
    filtr = driver.find_element(By.XPATH , XPATH_FILTER_BUTTON)
    filtr.click()
    filtr_hl = driver.find_element(By.XPATH , FILTER_HIGH_LOW)
    filtr_hl.click()

def list_names_items_on_page(driver):
    item_info = driver.find_element(By.XPATH, INFO_ALL_ITEMS_ON_PAGE)
    item_names = []
    for i in range(0,len(item_info.text.split('\n')),4):
        item_names.append(item_info.text.split('\n')[i])
    return item_names

def list_price_items_on_page(driver):
    item_info = driver.find_element(By.XPATH, INFO_ALL_ITEMS_ON_PAGE)
    item_price = []
    for i in range(2,len(item_info.text.split('\n')),4):
        item_price.append(float(item_info.text.split('\n')[i][1:]))
    return item_price
