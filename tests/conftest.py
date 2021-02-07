import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge", help="Available browser: chrome | firefox | edge"
    )


@pytest.fixture(scope="class")
def setup(request):

    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="..//drivers//chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="..//drivers//geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="..//drivers//msedgedriver.exe")

    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver

    yield
    driver.quit()
