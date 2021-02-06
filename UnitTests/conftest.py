import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup():
    print("This is start of fixture method")
    assert "secure area!" in "You logged into a secure area!"
    yield
    print("This is closure of fixture method")


@pytest.fixture
def login_data_provider():
    print("Creating test data")
    return ["tomsmith", "SuperSecretPassword!", "tomsmith1", "SuperSecretPassword!1"]
