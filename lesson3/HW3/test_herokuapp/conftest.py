import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def chrome_options():
    options = Options()
    options.add_argument('--headless')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def driver_w_iw(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(time_to_wait=100)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=15)
    return wait