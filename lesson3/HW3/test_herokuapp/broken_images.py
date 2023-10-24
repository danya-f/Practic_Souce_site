from selenium.webdriver.common.by import By

def test_find_broken_img(driver):
    driver.get("https://the-internet.herokuapp.com/broken_images")

    img = driver.find_elements(By.XPATH , "//div/img")
    print(len(img))
    bad_img =[]
    all_img = []
    for i in img:
        all_img.append(i.get_attribute("src"))
    for i in all_img:
        driver.get(i)
        if len(driver.find_elements(By.XPATH , '//*')) == 4:
            bad_img.append(i)
        driver.get("https://the-internet.herokuapp.com/broken_images")
    print(f"Плохие картинки : {bad_img}")