from selenium.webdriver.common.by import By

from Utils.LoggerUtil import LoggerUtil
from pages.HomePage import HomePage


class LoginPage(LoggerUtil):

    def __init__(self, driver):
        self.driver = driver

    username_txt = (By.ID, "txtUsername")
    password_txt = (By.ID, "txtPassword")
    login_btn = (By.ID, "btnLogin")
    login_image_container = (By.ID, "divLoginImageContainer")
    invalid_msg = (By.ID, "spanMessage")

    def setUsername(self, username):
        self.driver.find_element(*LoginPage.username_txt).send_keys(username)
        self.getLogger().info("Entered username")
        return self

    def setPassword(self, password):
        self.driver.find_element(*LoginPage.password_txt).send_keys(password)
        self.getLogger().info("Entered password")
        return self

    def clickLoginBtn(self):
        self.driver.find_element(*LoginPage.login_btn).click()
        self.getLogger().info("Clicked on Submit button")
        return HomePage(self.driver)

    def getLoginImageContainer(self):
        return self.driver.find_element(*LoginPage.login_image_container)

    def getInvalidMsgText(self):
        return self.driver.find_element(*LoginPage.invalid_msg).text
