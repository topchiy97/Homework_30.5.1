import pytest
from selenium import webdriver
from test_selenium_petfriends import base_url

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
    pytest.driver.get(f"{base_url} + login")
    pytest.driver.maximize_window()

    yield pytest.driver

    pytest.driver.quit()