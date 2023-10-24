from lesson3.HW3.test_victor_site.help_info.selectors import *
from selenium.webdriver.common.by import By
from time import sleep
from lesson3.HW3.test_victor_site.help_info.help_info import *
from selenium.webdriver.support import expected_conditions as EC




def test_auth_with_time_sleep(driver):
    driver.get(MANE_PAGE)
    assert driver.find_element(By.XPATH, TITLE).text == 'Практика с ожиданиями в Selenium'

    sleep(6)
    button_start_testing = driver.find_element(By.XPATH , BUTTON_START_TEST)
    button_start_testing.click()

    driver.find_element(By.XPATH ,LOGIN).send_keys('login')
    sleep(1)
    driver.find_element(By.XPATH , PASSWORD).send_keys('password')
    sleep(1)
    driver.find_element(By.XPATH , CHECK_BOX_AGREE).click()
    sleep(1)
    driver.find_element(By.XPATH , REGISTER_BUTTON).click()
    assert driver.find_element(By.XPATH, LOADER).is_displayed()
    sleep(5)
    assert driver.find_element(By.XPATH ,SUCCESS_MESSAGE).text=='Вы успешно зарегистрированы!' and driver.find_element(By.XPATH ,SUCCESS_MESSAGE).is_displayed()


def test_auth_with_implicit_waits(driver_w_iw):
    driver_w_iw.get(MANE_PAGE)
    assert driver_w_iw.find_element(By.XPATH, TITLE).text == 'Практика с ожиданиями в Selenium'
    button_start_testing = driver_w_iw.find_element(By.XPATH, BUTTON_START_TEST)
    button_start_testing.click()

    driver_w_iw.find_element(By.XPATH, LOGIN).send_keys('login')
    driver_w_iw.find_element(By.XPATH, PASSWORD).send_keys('password')
    driver_w_iw.find_element(By.XPATH, CHECK_BOX_AGREE).click()

    driver_w_iw.find_element(By.XPATH, REGISTER_BUTTON).click()

    assert driver_w_iw.find_element(By.XPATH, LOADER).is_enabled()

    success_msg = driver_w_iw.find_element(By.XPATH , SUCCESS_MESSAGE)
    success_msg.click()
    assert success_msg.is_displayed()
    assert success_msg.text == 'Вы успешно зарегистрированы!'


def test_auth_with_ec(driver, wait):

    driver.get(MANE_PAGE)
    assert driver.find_element(By.XPATH, TITLE).text == 'Практика с ожиданиями в Selenium'
    wait.until(EC.element_to_be_clickable((By.XPATH, BUTTON_START_TEST))).click()

    driver.find_element(By.XPATH, LOGIN).send_keys('login')
    driver.find_element(By.XPATH, PASSWORD).send_keys('password')
    driver.find_element(By.XPATH, CHECK_BOX_AGREE).click()
    driver.find_element(By.XPATH, REGISTER_BUTTON).click()

    assert wait.until(EC.element_to_be_clickable((By.XPATH, LOADER))).is_displayed()
    success_msg = wait.until(EC.element_to_be_clickable((By.XPATH,SUCCESS_MESSAGE)))
    assert success_msg.is_displayed()
    assert success_msg.text == 'Вы успешно зарегистрированы!'






