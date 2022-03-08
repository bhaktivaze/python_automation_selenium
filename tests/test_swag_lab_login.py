import time

import pytest
from selenium.common.exceptions import WebDriverException
from pages.swag_lab_login import SwagLabLoginPage
from pages.swag_inventory_page import SwagInventoryPage
from tests.basetest import BaseTest
from utils.ConfigReaderUtil import ConfigReaderUtil


class TestLogin(BaseTest):

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_login_swag(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()


        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "locked_out_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_login_swag_user_lockout(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            swagloginPageObject.click_login_button()
            userlockmessage = swagloginPageObject.verify_error_for_invalid_login()
            assert userlockmessage is True

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

