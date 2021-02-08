from selenium.webdriver.common.by import By

from Utils.LoggerUtil import LoggerUtil


class HomePage(LoggerUtil):
    def __init__(self, driver):
        self.driver = driver

    login_icon = (By.ID, "welcome")
    logout_link = (By.LINK_TEXT, "Logout")

    def getLoggedInMsg(self):
        return self.driver.find_element(*HomePage.login_icon)

    def doLogout(self):
        self.driver.find_element(*HomePage.login_icon).click()
        self.getLogger().info("Clicked on login user icon")
        self.driver.find_element(*HomePage.logout_link).click()
        self.getLogger().info("Clicked on logout link")
