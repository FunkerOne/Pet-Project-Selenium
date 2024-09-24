import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()
