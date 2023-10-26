import pytest
from selenium import webdriver
from faker import Faker
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

fake = Faker()


@pytest.fixture()
def chr_options():
    options = Options()
    options.add_argument('--headless')
    return options


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=15)
    return wait


@pytest.fixture()
def driver(chr_options):
    driver = webdriver.Chrome(options=chr_options)
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture()
def firstname():
    firstname = fake.name().split()[0]
    return firstname


@pytest.fixture()
def lastname():
    lastname = fake.name().split()[1]
    return lastname


@pytest.fixture()
def zipcode():
    zipcode = fake.zipcode()
    return zipcode


@pytest.fixture()
def email():
    email = fake.email()
    return email
