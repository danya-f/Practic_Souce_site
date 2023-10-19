from lesson1.help_files.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_add_item_from_catalog():
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
    login_and_add_2_item(driver)
    cart = driver.find_element(By.CSS_SELECTOR , CART)
    cart.click()
    sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'
    delete = driver.find_element(By.CSS_SELECTOR , DELETE_FROM_CART)
    delete.click()
    check_cart_items = driver.find_element(By.XPATH , XPATH_ITEMS_ON_SHOPPING_CART).text
    assert check_cart_items == '1'
    #проверил что кол-во товаров стало 1 после удаления,  вместо 2
    driver.quit()

def test_add_item_from_itemcard():
    driver = webdriver.Chrome()
    log_in(driver)
    item_1 = driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_1)
    item_1.click() #добавил товар в корзину что бы была нумерация товаров в корзине
    check_cart_items = driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text
    assert check_cart_items == '1'  # проверяем что товар есть один в корзине

    item_2 = driver.find_element(By.XPATH , XPATH_ONESIE_TITLE_LINK )
    item_2.click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=2' #проверяем что перешли в карточку товара

    add_to_cart_1 = driver.find_element(By.XPATH , XPATH_ONESIE_ADD_TO_CART_BUTTON)
    add_to_cart_1.click()
    check_cart_items = driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text
    assert check_cart_items == '2' #проверяем что количество товаров изменилось в корзине после добавления

    delete_from_cart = driver.find_element(By.XPATH, XPATH_ONESIE_DELETE_FROM_CART_BUTTON)
    delete_from_cart.click()
    check_cart_items = driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text
    assert check_cart_items == '1'
    driver.quit()

def test_delete_item_from_itemcard():
    driver = webdriver.Chrome()
    log_in(driver)
    item_1 = driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_1)
    item_1.click()  # добавил товар в корзину что бы была нумерация товаров в корзине
    check_cart_items = driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text
    sleep(1)
    assert check_cart_items == '1'  # проверяем что товар есть один в корзине

    item_2 = driver.find_element(By.XPATH, XPATH_ONESIE_TITLE_LINK)
    item_2.click()
    sleep(1)
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=2'  # проверяем что перешли в карточку товара

    add_to_cart_1 = driver.find_element(By.XPATH, XPATH_ONESIE_ADD_TO_CART_BUTTON)
    add_to_cart_1.click()
    check_cart_items = driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text
    sleep(1)
    assert check_cart_items == '2'  # проверяем что количество товаров изменилось в корзине после добавления

    delete_from_cart = driver.find_element(By.XPATH, XPATH_ONESIE_DELETE_FROM_CART_BUTTON)
    delete_from_cart.click()
    check_cart_items = driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text
    sleep(1)
    assert check_cart_items == '1' # проверяем что количество товаров изменилось в корзине после удаления
    driver.quit()