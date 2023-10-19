from lesson1.help_files.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By





def test_burger_logout():
    driver = webdriver.Chrome()
    log_in(driver)

    burger_menu = driver.find_element(By.XPATH , BURGER_MENU)
    burger_menu.click()
    sleep(1)

    logout_button = driver.find_element(By.XPATH , LOGOUT_BUTTON_FROM_BURGER_MENU)
    logout_button.click()
    sleep(2)

    assert driver.current_url == 'https://www.saucedemo.com/'
    driver.quit()

def test_burger_about():
    driver = webdriver.Chrome()
    log_in(driver)

    burger_menu = driver.find_element(By.XPATH , BURGER_MENU)
    burger_menu.click()
    sleep(1)

    about_button = driver.find_element(By.XPATH , ABOUT_BUTTON_FROM_BURGER_MENU)
    about_button.click()
    sleep(1)
    driver.find_element(By.TAG_NAME, "body").send_keys("Keys.ESCAPE")
    assert driver.current_url == 'https://saucelabs.com/'

def test_burger_reset_app():
    driver = webdriver.Chrome()
    login_and_add_2_item(driver)

    burger_menu = driver.find_element(By.XPATH , BURGER_MENU)
    burger_menu.click()
    sleep(1)
    reset_app_button = driver.find_element(By.XPATH , RESET_APP_BUTTON)
    reset_app_button.click()
    sleep(1)
    add_item = driver.find_element(By.XPATH , ADD_TO_CART_3).click()
    sleep(2)
    count_items_on_cart = driver.find_element(By.XPATH , XPATH_ITEMS_ON_SHOPPING_CART)
    assert count_items_on_cart.text == '1'