import requests
from selenium.webdriver.common.by import By

def test_find_broken_img(driver):
    driver.get("https://the-internet.herokuapp.com/broken_images")

    img = driver.find_elements(By.XPATH , "//div/img")
    all_img = []
    for i in img:
        all_img.append(i.get_attribute("src"))
    bad_img = []
    for i in all_img:
        if requests.get(i).status_code == 404:
            bad_img.append(i)
    print()
    print(f"Плохие картинки : {bad_img}")