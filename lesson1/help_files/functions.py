from selenium.webdriver.common.by import By
from time import sleep
from lesson1.help_files.auth_info import *
from lesson1.help_files.selectors import *


def log_in(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.CSS_SELECTOR, USER_NAME).send_keys(standart_login)

    driver.find_element(By.CSS_SELECTOR, PASSWORD).send_keys(password)

    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()
    sleep(1)

    assert driver.current_url == URL_AFTER_LOGIN




def login_and_add_2_item(driver):
    log_in(driver)
    driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_1).click()
    sleep(1)
    assert driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text == "1"
    driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_2).click()
    sleep(1)
    assert driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text == '2'


def go_to_cart(driver):
    driver.find_element(By.XPATH , XPATH_SHOPPING_CART).click()
    assert driver.current_url == URL_CART


def push_checkout(driver):
    driver.find_element(By.XPATH , XPATH_CHECKOUT_BUTTON_ON_CART).click()


def enter_info_checkout_step_1(driver,firstname,lastname,zipcode):
    driver.find_element(By.XPATH , XPATH_ENTER_FIRSTNAME).send_keys(firstname)
    driver.find_element(By.XPATH , XPATH_ENTER_LASTNAME).send_keys(lastname)
    driver.find_element(By.XPATH , XPATH_ENTER_ZIPCODE).send_keys(zipcode)


def push_continue_on_checkout(driver):
    driver.find_element(By.XPATH , XPATH_CONTINUE_BUTTON).click()


def push_finish_on_checkout(driver):
    driver.find_element(By.XPATH , XPATH_FINISH_BUTTON_ON_CHECKOUT).click()

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
