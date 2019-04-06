from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def driver_init(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(15)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
        