from lesson1.help_files.functions import *
from selenium.webdriver.common.by import By



def test_checkout(driver,firstname,lastname,zipcode):
    login_and_add_2_item(driver)
    go_to_cart(driver)

    push_checkout(driver)
    assert driver.current_url == URL_1STEP_CHECKOUT

    enter_info_checkout_step_1(driver,firstname,lastname,zipcode)
    push_continue_on_checkout(driver)
    assert driver.current_url == URL_2STEP_CHECKOUT

    push_finish_on_checkout(driver)
    assert driver.find_element(By.XPATH , CONFIRM_ORDER_TEXT).text == 'Thank you for your order!'





