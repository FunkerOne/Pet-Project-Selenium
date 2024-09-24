from selenium.webdriver.common.by import By


class SignInPage:

    _USER_NAME_FIELD = (By.ID, 'user-name')
    _PASSWORD_FIELD = (By.ID, 'password')
    _SIGN_IN_BUTTON = (By.ID, 'login-button')
    _ERROR_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    def __init__(self, driver) -> None:
        self.driver = driver

    def fill_user_name(self, user_name: str) -> None:
        self.driver.find_element(*self._USER_NAME_FIELD).send_keys(user_name)

    def fill_password(self, password: str) -> None:
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)

    def click_sign_in_button(self) -> None:
        self.driver.find_element(*self._SIGN_IN_BUTTON).click()

    def get_error_message_text(self):
        return self.driver.find_element(*self._ERROR_MESSAGE).text

    def sign_in(self, user_name: str, password: str) -> None:
        self.fill_user_name(user_name)
        self.fill_password(password)
        self.click_sign_in_button()
