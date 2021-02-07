import pytest


@pytest.fixture(scope="class")
def setup():
    print("This is start of fixture method")
    assert "secure area!" in "You logged into a secure area!"
    yield
    print("This is closure of fixture method")


@pytest.fixture(params=["chrome", "firefox", "edge"])
def data_list(request):
    return request.param


@pytest.fixture(params=[
    ("browser", "chrome", "tomsmith", "SuperSecretPassword!"),
    ("browser", "firefox", "foo", "baar")
])
def data_list_of_tuple(request):
    return request.param

