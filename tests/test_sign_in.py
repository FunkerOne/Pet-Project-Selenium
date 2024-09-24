import pytest
from pages.sign_in_page import SignInPage
from pages.home_page import HomePage


class TestSignIn:
    @pytest.mark.parametrize('user_name, password', [('standard_user', 'secret_sauce'),
                                                     ('problem_user', 'secret_sauce'),
                                                     ('performance_glitch_user', 'secret_sauce'),
                                                     ('error_user', 'secret_sauce'),
                                                     ('visual_user', 'secret_sauce')])
    def test_success_sign_in(self, user_name, password, driver):
        sign_in_page = SignInPage(driver)
        sign_in_page.sign_in(user_name, password)
        header_logo = HomePage(driver)
        header_logo.wait_for_load_head_logo()
        logo_text_from_header_logo = header_logo.get_logo_text()
        assert logo_text_from_header_logo == 'Swag Labs'

    def test_unsuccess_sing_in(self, driver):
        sign_in_page = SignInPage(driver)
        user_name = 'invalid_user_name'
        password = 'secret_sauce'
        sign_in_page.sign_in(user_name, password)
        error_text = sign_in_page.get_error_message_text()
        assert error_text == 'Epic sadface: Username and password do not match any user in this service'
