import pytest

from TestData.HomePageData import HomePageData
from Utils.BaseClass import BaseClass
from pages.LoginPage import LoginPage


class TestLoginLogout(BaseClass):

    def test_e2e(self, login_data):
        home_page = LoginPage(self.driver).setUsername(login_data["username"]).setPassword(login_data["password"]).clickLoginBtn()
        assert ("Welcome" in home_page.getLoggedInMsg().text)

        home_page.doLogout()
        assert LoginPage(self.driver).getLoginImageContainer().is_displayed() == True

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def login_data(self, request):
        return request.param
