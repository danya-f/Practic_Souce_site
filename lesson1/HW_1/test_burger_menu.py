from lesson1.help_files.functions import *
from selenium.webdriver.common.by import By





def test_burger_logout(driver):
    log_in(driver)

    driver.find_element(By.XPATH , BURGER_MENU).click()
    sleep(1)

    driver.find_element(By.XPATH , LOGOUT_BUTTON_FROM_BURGER_MENU).click()
    sleep(1)

    assert driver.current_url == MAIN_PAGE

def test_burger_about(driver):
    log_in(driver)

    driver.find_element(By.XPATH , BURGER_MENU).click()
    sleep(1)

    driver.find_element(By.XPATH , ABOUT_BUTTON_FROM_BURGER_MENU).click()
    sleep(3)
    # driver.find_element(By.TAG_NAME, "body").send_keys("Keys.ESCAPE")
    assert driver.current_url == 'https://saucelabs.com/'

def test_burger_reset_app(driver):
    login_and_add_2_item(driver)

    driver.find_element(By.XPATH , BURGER_MENU).click()
    sleep(1)
    driver.find_element(By.XPATH , RESET_APP_BUTTON).click()
    sleep(1)
    driver.find_element(By.XPATH , ADD_TO_CART_3).click()
    sleep(1)

    assert driver.find_element(By.XPATH , XPATH_ITEMS_ON_SHOPPING_CART).text == '1'