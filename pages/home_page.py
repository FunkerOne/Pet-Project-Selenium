from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    _HEADER_LOGO = (By.CLASS_NAME, 'app_logo')

    def __init__(self, driver) -> None:
        self.driver = driver

    def wait_for_load_head_logo(self) -> None:
        WebDriverWait(self.driver, 1).until(ec.visibility_of_element_located(self._HEADER_LOGO))

    def get_logo_text(self):
        return self.driver.find_element(*self._HEADER_LOGO).text
