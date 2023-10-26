from lesson1.help_files.functions import *
from selenium.webdriver.common.by import By





def test_go_to_item_from_image(driver):
    log_in(driver)
    driver.find_element(By.XPATH , XPATH_BIKE_IMG_LINK).click()
    sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0'

def test_go_to_item_from_title(driver):
    log_in(driver)
    driver.find_element(By.XPATH , XPATH_ONESIE_TITLE_LINK).click()
    sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=2'