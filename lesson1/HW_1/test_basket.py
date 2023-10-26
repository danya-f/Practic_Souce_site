from lesson1.help_files.functions import *
from selenium.webdriver.common.by import By



def test_add_item_from_catalog(driver):
    log_in(driver)
    driver.find_element(By.CSS_SELECTOR , ID_ADD_TO_CART_1).click()
    sleep(1)
    assert driver.find_element(By.XPATH , XPATH_ITEMS_ON_SHOPPING_CART).text == "1"

    driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_2).click()
    sleep(1)
    assert driver.find_element(By.XPATH , XPATH_ITEMS_ON_SHOPPING_CART).text == '2'


def test_delete_item_from_cart(driver):

    login_and_add_2_item(driver)
    driver.find_element(By.CSS_SELECTOR, CART).click()
    sleep(2)

    assert driver.current_url == URL_CART
    assert driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text == "2"

    driver.find_element(By.CSS_SELECTOR, DELETE_FROM_CART).click()
    assert driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text == "1"
    #проверил что кол-во товаров стало 1 после удаления,  вместо 2

def test_add_item_from_itemcard(driver):
    log_in(driver)
    driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_1).click()
    #добавил товар в корзину что бы была нумерация товаров в корзине

    assert driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text == '1'  # проверяем что товар есть один в корзине

    driver.find_element(By.XPATH , XPATH_ONESIE_TITLE_LINK ).click()
    assert driver.current_url == ONESIE_ITEM_CARD
    #проверяем что перешли в карточку товара

    driver.find_element(By.XPATH , XPATH_ONESIE_ADD_TO_CART_BUTTON).click()
    assert driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text == '2'
    #проверяем что количество товаров изменилось в корзине после добавления товара

    driver.find_element(By.XPATH, XPATH_ONESIE_DELETE_FROM_CART_BUTTON).click()
    assert driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text == '1'


def test_delete_item_from_itemcard(driver):
    log_in(driver)
    driver.find_element(By.CSS_SELECTOR, ID_ADD_TO_CART_1).click()
    # добавил товар в корзину что бы была нумерация товаров в корзине
    sleep(1)
    assert driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text == '1'
    # проверяем что товар есть один в корзине

    driver.find_element(By.XPATH, XPATH_ONESIE_TITLE_LINK).click()
    sleep(1)
    assert driver.current_url == ONESIE_ITEM_CARD
    # проверяем что перешли в карточку товара

    driver.find_element(By.XPATH, XPATH_ONESIE_ADD_TO_CART_BUTTON).click()
    sleep(1)
    assert driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text == '2'
    # проверяем что количество товаров изменилось в корзине после добавления

    driver.find_element(By.XPATH, XPATH_ONESIE_DELETE_FROM_CART_BUTTON).click()
    sleep(1)
    assert driver.find_element(By.XPATH, XPATH_ITEMS_ON_SHOPPING_CART).text == '1'
    # проверяем что количество товаров изменилось в корзине после удаления