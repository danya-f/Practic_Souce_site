from lesson1.help_files.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_filter_A_Z():
    driver = webdriver.Chrome()
    log_in(driver)

    push_filter_A_Z(driver)
    sleep(2)
    name_ot_A_Z = driver.find_element(By.XPATH , XPATH_ALL_ITEM_ON_PAGE)
    item_names = list(list_names_items_on_page(driver))
    assert name_ot_A_Z.text == sorted(item_names)[0]

def test_filter_Z_A():
    driver = webdriver.Chrome()
    log_in(driver)

    push_filter_Z_A(driver)
    sleep(2)
    name_ot_Z_A = driver.find_element(By.XPATH , XPATH_ALL_ITEM_ON_PAGE)
    item_names = list(list_names_items_on_page(driver))
    assert name_ot_Z_A.text == sorted(item_names)[-1]


def test_filter_low_high():
    driver = webdriver.Chrome()
    log_in(driver)

    push_filter_low_high(driver)
    sleep(2)
    item_price = list(list_price_items_on_page(driver))
    first_item_price = driver.find_element(By.XPATH, PRICE_ITEMS_ON_CATALOG)
    assert first_item_price.text == f'${str(sorted(item_price)[0])}'


def test_filter_high_low():
    driver = webdriver.Chrome()
    log_in(driver)

    push_filter_high_low(driver)
    sleep(2)
    item_price = list(list_price_items_on_page(driver))
    first_item_price = driver.find_element(By.XPATH, PRICE_ITEMS_ON_CATALOG)
    assert first_item_price.text == f'${str(sorted(item_price)[-1])}'

def test_inventory_list():
    driver = webdriver.Chrome()
    log_in(driver)

    push_filter_high_low(driver)
    sleep(1)
    item_names = list(list_names_items_on_page(driver))
    print(item_names)
    item_price = list(list_price_items_on_page(driver))
    print(item_price)


