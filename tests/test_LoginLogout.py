import pytest

from TestData.HomePageData import HomePageData
from Utils.ExcelReader import ExcelReader
from Utils.BaseClass import BaseClass
from pages.LoginPage import LoginPage


class TestLoginLogout(BaseClass):

    def test_LoginLogout(self, login_data):
        home_page = LoginPage(self.driver).setUsername(login_data["Username"]).setPassword(
            login_data["Password"]).clickLoginBtn()
        assert ("Welcome" in home_page.getLoggedInMsg().text)

        home_page.doLogout()
        assert LoginPage(self.driver).getLoginImageContainer().is_displayed() == True

    def test_InvalidLogin(self, invalid_login_data):
        LoginPage(self.driver).setUsername(invalid_login_data["Username"]).setPassword(
            invalid_login_data["Password"]).clickLoginBtn()
        assert (LoginPage(self.driver).getInvalidMsgText() == "Invalid credentials")

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def login_data(self, request):
        return request.param

    @pytest.fixture(params=ExcelReader.get_excel_data_as_dictionary("test_InvalidLogin"))
    def invalid_login_data(self, request):
        return request.param
