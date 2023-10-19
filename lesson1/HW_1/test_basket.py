from lesson1.help_files.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_add_item():
    driver = webdriver.Chrome()
    log_in(driver)
    add_item_button_1 = driver.find_element(By.CSS_SELECTOR , ID_ADD_TO_CART_1)
    add_item_button_1.click()
    sleep(1)
    a = driver.find_element(By.XPATH , XPATH_ITEMS_ON_SHOPPING_CART)
    add_item_button_2 = driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_2)
    add_item_button_2.click()
    sleep(1)
    assert a.text == '2'

    driver.quit()

def test_delete_item_from_cart():
    driver = webdriver.Chrome()
    add_2_item(driver)
    cart = driver.find_element(By.CSS_SELECTOR , CART)
    cart.click()
    sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'
    delete = driver.find_element(By.CSS_SELECTOR , DELETE_FROM_CART)
    delete.click()
    check_cart_items = driver.find_element(By.XPATH , XPATH_ITEMS_ON_SHOPPING_CART).text
    assert check_cart_items == '1'
    assert check_cart_items == '2'
    #проверил что равно 1 после удаления