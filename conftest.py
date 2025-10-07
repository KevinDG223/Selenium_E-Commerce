import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default = "edge", help = "browser selection")


@pytest.fixture(scope = "function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "edge":
        driver = webdriver.Edge()
        driver.maximize_window()

    elif browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.close()