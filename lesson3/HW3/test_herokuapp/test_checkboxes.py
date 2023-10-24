from selenium.webdriver.common.by import By

def test_checkbox(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    assert driver.find_element(By.XPATH , "(//*[@type = 'checkbox'])[1]")
