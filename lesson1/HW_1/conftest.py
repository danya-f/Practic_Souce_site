import pytest
from selenium import webdriver
from faker import Faker
fake = Faker()


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture()
def fake_info_for_order():
    firstname = fake.name().split()[0]
    lastname = fake.name().split()[1]
    zipcode = fake.zipcode()
    email = fake.email()