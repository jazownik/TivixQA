from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def setup_test_page():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.tivix.com/")
    yield driver
    driver.close()
