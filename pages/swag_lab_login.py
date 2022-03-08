from selenium.webdriver.common.by import By
from pages.createaccount_page import CreateAccountPage
from pages.myaccount_page import MyAccountPage
from locators import swag_lab_login_page_locators
from pages.base_page import BasePage
from pages.swag_inventory_page import SwagInventoryPage


class SwagLabLoginPage(BasePage):

    def __init__(self, x, filepath):
        self.driver = x
        self.filepath = filepath
        self.locator = swag_lab_login_page_locators
        super().__init__(self.driver, self.filepath)

    def navigateToApplication(self, url):
        BasePage.navigateto(self, url)
        BasePage.page_has_loaded(self)
        return self

    def enterUserName(self, username):
        BasePage.entertext(self, By.ID, self.locator.SwagLabLoginLocator.USERNAME, username)
        return self

    def enterPassword(self, password):
        BasePage.entertext(self, By.ID, self.locator.SwagLabLoginLocator.PASSWORD, password)
        return self

    def click_login_button(self):
        BasePage.click(self, By.ID, self.locator.SwagLabLoginLocator.LOGINBUTTON)
        BasePage.page_has_loaded(self)
        inventorypage = SwagInventoryPage(self.driver, self.filepath)
        return inventorypage

    def verify_error_for_invalid_login(self):
        return BasePage.isElementPresent(self, By.XPATH, self.locator.SwagLabLoginLocator.USER_LOCK_ERROR)
