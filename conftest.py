import pytest
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def driver():
    # options = Options()
    # options.headless = True
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()