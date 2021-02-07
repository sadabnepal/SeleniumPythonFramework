from Utils.BaseClass import BaseClass
from pages.LoginPage import LoginPage


class TestLoginLogout(BaseClass):

    def test_e2e(self):
        home_page = LoginPage(self.driver).setUsername("Admin").setPassword("admin123").clickLoginBtn()
        assert self.verifyLink("Welcome Paul").is_displayed() == True
        assert ("Welcome" in home_page.getLoggedInMsg().text)

        home_page.doLogout()
        assert LoginPage(self.driver).getLoginImageContainer().is_displayed() == True


