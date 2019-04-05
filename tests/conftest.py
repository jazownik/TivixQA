from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def setup_test_page():
    driver = webdriver.Chrome()
    driver.get("www.tivix.com")
    yield driver
    driver.close()
