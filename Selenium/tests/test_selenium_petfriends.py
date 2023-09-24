import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password

base_url = "http://petfriends.skillfactory.ru/"


def test_show_all_pets():

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\col-sm-4.left"))
    )
    statistics = pytest.driver.find_element(By.CSS_SELECTOR, ".\\col-sm-4.left")

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table.table-hover tbody tr"))
    )

    pets = pytest.driver.find_element(By.CSS_SELECTOR, "table.table-hover tbody tr")

    number = statistics[0].text.split("\n")
    number = number[1].split(" ")
    number = number[-1].split(" ")
    number = int(number)

    number_of_pets = len(pets)
    assert number ==  number_of_pets

    email_imput = pytest.driver.find_element(By.ID, "email")
    email_imput.send_keys(valid_email)

    pass_imput = pytest.driver.find_element(By.ID, "pass")
    pass_imput.send_keys(valid_password)

    pytest.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert pytest.driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"

    pytest.driver.get(f"{base_url}")

    images = pytest.driver.find_elements_by_css_selector(".card-deck .card-img-top")
    names = pytest.driver.find_elements_by_css_selector(".card-deck .card-title")
    descriptions = pytest.driver.find_elements_by_css_selector(".card-deck .card-text")

    for i in range(len(names)):
        assert images[i].get_attribute("src") != ""
        assert names[i].text != ""
        assert descriptions[i].text != ""
        assert ", " in descriptions[i]

        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0