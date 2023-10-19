from lesson1.help_files.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

def test_checkout():
    driver = webdriver.Chrome()
    login_and_add_2_item(driver)
    go_to_cart(driver)
    sleep(1)
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'

    push_checkout(driver)
    sleep(1)
    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html'

    enter_info_checkout_step_1(driver)
    sleep(1)
    push_continue_on_checkout(driver)
    sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-two.html'

    push_finish_on_checkout(driver)
    sleep(2)
    checkout_done = driver.find_element(By.XPATH , "//h2[@class = 'complete-header']")
    assert checkout_done.text == 'Thank you for your order!'





