import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(10)
    return driver
