from selenium.webdriver.common.by import By
from pages.HomePage import HomePage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_txt = (By.ID, "txtUsername")
    password_txt = (By.ID, "txtPassword")
    login_btn = (By.ID, "btnLogin")
    login_image_container = (By.ID, "divLoginImageContainer")

    def setUsername(self, username):
        self.driver.find_element(*LoginPage.username_txt).send_keys(username)
        return self

    def setPassword(self, password):
        self.driver.find_element(*LoginPage.password_txt).send_keys(password)
        return self

    def clickLoginBtn(self):
        self.driver.find_element(*LoginPage.login_btn).click()
        return HomePage(self.driver)

    def getLoginImageContainer(self):
        return self.driver.find_element(*LoginPage.login_image_container)
