import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_condition


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, link_text):
        element = WebDriverWait(self.driver, 10).until(
            expected_condition.presence_of_element_located((By.LINK_TEXT, link_text))
        )
        return element
