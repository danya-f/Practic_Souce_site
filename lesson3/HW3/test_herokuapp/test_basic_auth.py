from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_auth(driver, wait):
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    assert wait.until(EC.visibility_of(driver.find_element(By.XPATH, "//p")))
    assert driver.find_element(By.XPATH , "//p").text == "Congratulations! You must have the proper credentials."


