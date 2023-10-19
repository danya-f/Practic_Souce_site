from lesson1.help_files.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By





def test_go_to_item_from_image():
    driver = webdriver.Chrome()
    log_in(driver)
    image_item = driver.find_element(By.XPATH , XPATH_BIKE_IMG_LINK)
    image_item.click()
    sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0'

def test_go_to_item_from_title():
    driver = webdriver.Chrome()
    log_in(driver)
    item_title = driver.find_element(By.XPATH , XPATH_ONESIE_TITLE_LINK)
    item_title.click()
    sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=2'