import pytest
from selenium import webdriver

from Utils.LoggerUtil import LoggerUtil


class TestLoginLogout(LoggerUtil):

    def test_login_with_data_provider(self, login_data_provider):
        driver = webdriver.Edge(executable_path="E:\\ProjectsWIP\\SeleniumPythonFramework\\drivers\\msedgedriver.exe")
        driver.implicitly_wait(30)
        log = self.getLogger()

        log.info("Opening URL....")
        driver.get("https://the-internet.herokuapp.com")
        driver.maximize_window()
        log.info("Maximizing window")
        print("URL of the page: ", driver.current_url)
        print("Title of the page: ", driver.title)

        driver.find_element_by_link_text("Form Authentication").click()
        log.info("Clicking on Form Authentication")
        driver.find_element_by_id("username").send_keys(login_data_provider[0])
        log.info("Entering username")
        driver.find_element_by_id("password").send_keys(login_data_provider[1])
        log.info("Entering password")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        log.info("Clicked on Submit button")

        login_message = driver.find_element_by_id("flash").text
        assert "You logged into a secure area!" in login_message
        log.info("Login successfully validated")
        driver.quit()
        log.info("Browser closed!!!")

    @pytest.mark.smoke
    def test_tag_method(self, login_data_provider):
        print("Valid User Name: "+login_data_provider[0])
        print("Valid Password Name: " + login_data_provider[1])
        print("Invalid User Name: " + login_data_provider[2])
        print("Invalid Password Name: " + login_data_provider[3])

    @pytest.mark.xfail
    def test_ignore_in_result(self):
        print("This will fail, but will not be included in report")
        greet = "Good Morning"
        assert greet == "Good", "Failed as greet value did not match"

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_skip_method(self):
        print("This will be skipped")
        a = 4
        b = 10
        assert b == a + 6, "Addition validation failed"
