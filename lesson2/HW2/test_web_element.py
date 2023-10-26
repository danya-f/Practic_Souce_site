from info import *
from selenium.webdriver.common.by import By

def test_web_elem(driver):
    driver.get(MAIN_PAGE)
    assert driver.current_url == MAIN_PAGE

    assert driver.find_element(By.XPATH , BUTTON).get_attribute("disabled") == 'true'

    driver.find_element(By.XPATH , USERNAME).send_keys('user')
    driver.find_element(By.XPATH, PASSWORD).send_keys('password')
    driver.find_element(By.XPATH, CHECK_BOX).click()

    assert driver.find_element(By.XPATH, BUTTON).get_attribute("disabled") == None
