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
    def test_inventory_sort_hilo(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.select_inventory_filter('hilo')
            inventorypage.verify_inventory_sorting()
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()


        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_add_to_cart(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_addtocart_lick()
            inventorypage.clik_remove_button()
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_inventory_sort_atoz(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.select_inventory_filter('za')
            inventorypage.verify_inventory_sorting()
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()


        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_navigate_Product_details(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_addtocart_lick()
            inventorypage.clik_cart_icon()
            productNavigationPageisNavigated = inventorypage.verifyProductDetailsPageNavigation()
            assert productNavigationPageisNavigated is True
            inventorypage.clik_remove_button()
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_navigate_Product_listing_from_product_details(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_product_link()
            inventorypage.clik_back_to_products_link()
            verifyInventoryPage = inventorypage.verifyInventoryPage()
            assert verifyInventoryPage is True
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_navigate_Product_details_AddToCart_continue_shopping(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_addtocart_lick()
            inventorypage.clik_cart_icon()
            productNavigationPageisNavigated = inventorypage.verifyProductDetailsPageNavigation()
            assert productNavigationPageisNavigated is True
            inventorypage.clik_continue_shopping()
            inventorypage.clik_remove_button()
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_add_more_products_to_cart(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_addtocart_lick()
            inventorypage.clik_cart_icon()
            productNavigationPageisNavigated = inventorypage.verifyProductDetailsPageNavigation()
            assert productNavigationPageisNavigated is True
            inventorypage.clik_remove_button()
            inventorypage.clik_continue_shopping()
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_remove_products(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_addtocart_lick()
            inventorypage.clik_cart_icon()
            inventorypage.clik_remove_button()
            carthasitems = inventorypage.verifY_cart_empty()
            assert carthasitems is False
            inventorypage.clik_continue_shopping()
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_checout_process(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_addtocart_lick()
            inventorypage.clik_cart_icon()
            inventorypage.clik_checkout_button()
            checkouPageNavigation = inventorypage.verifyCheckoutPageNavigation()
            assert checkouPageNavigation is True
            inventorypage.clik_cart_icon()
            inventorypage.clik_remove_button()
            carthasitems = inventorypage.verifY_cart_empty()
            assert carthasitems is False
            inventorypage.clik_continue_shopping()
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_checout_process_personal_info(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_addtocart_lick()
            inventorypage.clik_cart_icon()
            inventorypage.clik_checkout_button()
            checkouPageNavigation = inventorypage.verifyCheckoutPageNavigation()
            assert checkouPageNavigation is True
            inventorypage.enterFirstName("Bhakti")
            inventorypage.enterLastName("Agashe")
            inventorypage.enterZip("411045")
            inventorypage.clik_continue_button()
            inventorypage.clik_cart_icon()
            inventorypage.clik_remove_button()
            carthasitems = inventorypage.verifY_cart_empty()
            assert carthasitems is False
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_checout_page_to_product_Page(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_addtocart_lick()
            inventorypage.clik_cart_icon()
            inventorypage.clik_checkout_button()
            checkouPageNavigation = inventorypage.verifyCheckoutPageNavigation()
            assert checkouPageNavigation is True
            inventorypage.click_cancel_button()
            inventorypage.clik_cart_icon()
            inventorypage.clik_remove_button()
            carthasitems = inventorypage.verifY_cart_empty()
            assert carthasitems is False
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_burger_menu(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_addtocart_lick()
            inventorypage.clik_cart_icon()
            inventorypage.clik_checkout_button()
            checkouPageNavigation = inventorypage.verifyCheckoutPageNavigation()
            assert checkouPageNavigation is True
            inventorypage.click_cancel_button()

            inventorypage.clik_cart_icon()
            inventorypage.clik_remove_button()
            carthasitems = inventorypage.verifY_cart_empty()
            assert carthasitems is False
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_all_items()
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e

    @pytest.mark.parametrize("test_loginMulUsers", [
        {"username": "standard_user", "pwd": "secret_sauce"}
    ], indirect=True)
    def test_Navigate_your_cart(self, test_loginMulUsers):
        try:
            name, pwd = test_loginMulUsers
            swagloginPageObject = SwagLabLoginPage(self.driver, self.filePath)
            swagloginPageObject.navigateToApplication(ConfigReaderUtil.get_env_value('baseUrl'))
            swagloginPageObject.enterUserName(name)
            swagloginPageObject.enterPassword(pwd)
            inventorypage = swagloginPageObject.click_login_button()
            loginsuccess = inventorypage.verifyInventoryPage()
            assert loginsuccess is True
            inventorypage.clik_addtocart_lick()
            inventorypage.clik_cart_icon()
            inventorypage.clik_remove_button()
            carthasitems = inventorypage.verifY_cart_empty()
            assert carthasitems is False
            inventorypage.clik_main_menu()
            time.sleep(3)
            inventorypage.clik_logout_lick()

        except WebDriverException as e:
            BaseTest.take_screenshot(self, e.msg)
            raise e