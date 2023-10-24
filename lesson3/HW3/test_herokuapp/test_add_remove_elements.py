from lesson3.HW3.test_herokuapp.help_info.selectors import *
from selenium.webdriver.common.by import By


def test_add_remove(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    assert len(driver.find_elements(By.XPATH, DELETE)) == 0

    driver.find_element(By.XPATH , ADD).click()
    assert len(driver.find_elements(By.XPATH ,DELETE )) == 1

    driver.find_element(By.XPATH, DELETE).click()
    assert len(driver.find_elements(By.XPATH, DELETE)) == 0


