from selenium.webdriver.common.by import By
from lesson3.HW3.test_herokuapp.help_info.selectors import *


def test_checkbox(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    assert driver.current_url == "https://the-internet.herokuapp.com/checkboxes"

    all_checkbox = driver.find_elements(By.XPATH , ALL_CHECKBOX)
    status = []
    for i in all_checkbox:
        status.append(i.get_attribute("checked"))
    for i in all_checkbox:
        i.click()
    new_status = []
    for i in all_checkbox:
        new_status.append(i.get_attribute("checked"))
    count = 0
    for i,j in new_status,status:
        if (i == 'true' and j == None) or (i == None and j == 'true'):
            continue
        else:
            count+=1
    assert count == 0


