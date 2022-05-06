import selenium
from selenium.webdriver.common.by import By

import locators
from locators import swag_lab_login_page_locators
from locators import swag_inventory_locator
from pages.base_page import BasePage


class SwagInventoryPage(BasePage):

    def __init__(self, x, filepath):
        self.driver = x
        self.filepath = filepath
        self.locator = locators.swag_inventory_locator
        super().__init__(self.driver, self.filepath)

    def verifyInventoryPage(self):
        inventorypageverification = BasePage.isDisplayed(self, By.XPATH, self.locator.SwagInventoryPage.PRODUCTS)
        return inventorypageverification

    def clik_main_menu(self):
        BasePage.click(self, By.ID, self.locator.SwagInventoryPage.MAIN_MENU)

    def clik_logout_lick(self):
        BasePage.click(self, By.ID, self.locator.SwagInventoryPage.LOGOUT_LINK)

    def select_inventory_filter(self, filtertype):
        if (filtertype == 'az'):
            BasePage.selectdropdownvaluebytext(self, By.CLASS_NAME,
                                               self.locator.SwagInventoryPage.CLASS_INVENTORY_FILTER_SELECT,
                                               'Name (A to Z)')
        elif (filtertype == 'za'):
            BasePage.selectdropdownvaluebytext(self, By.CLASS_NAME,
                                               self.locator.SwagInventoryPage.CLASS_INVENTORY_FILTER_SELECT,
                                               'Name (Z to A)')
        elif (filtertype == 'lohi'):
            BasePage.selectdropdownvaluebytext(self, By.CLASS_NAME,
                                               self.locator.SwagInventoryPage.CLASS_INVENTORY_FILTER_SELECT,
                                               'Price (low to high)')
        elif (filtertype == 'hilo'):
            BasePage.selectdropdownvaluebytext(self, By.CLASS_NAME,
                                               self.locator.SwagInventoryPage.CLASS_INVENTORY_FILTER_SELECT,
                                               'Price (high to low)')

    def verify_inventory_sorting(self):
        pricelistFinal = []
        flag = False
        pricelist = BasePage.getElementList(self, By.XPATH,
                                            self.locator.SwagInventoryPage.CLASS_INVENTORY_PIRCE_OF_ITEMS)

        print(pricelist)
        for i in pricelist:
            pricelistFinal.append(float(i[1:]))

        print(pricelistFinal)

        if pricelistFinal == sorted(pricelistFinal, reverse=True):
            flag = True
            assert flag is True

    def clik_addtocart_lick(self):
        BasePage.click(self, By.XPATH, self.locator.SwagInventoryPage.ADD_TO_CART_LINK)

    def clik_cart_icon(self):
        BasePage.click(self, By.XPATH, self.locator.SwagInventoryPage.CART_Link)

    def verifyProductDetailsPageNavigation(self):
        return BasePage.isElementPresent(self, By.XPATH, self.locator.SwagInventoryPage.YOUR_CART)

    def clik_remove_button(self):
        BasePage.click(self, By.XPATH, self.locator.SwagInventoryPage.REMOVE_BUTTON)

    def clik_product_link(self):
        BasePage.click(self, By.XPATH, self.locator.SwagInventoryPage.PRODUCT_LINK)

    def clik_back_to_products_link(self):
        BasePage.click(self, By.XPATH, self.locator.SwagInventoryPage.BACK_TO_PRODUCT)

    def clik_continue_shopping(self):
        BasePage.click(self, By.XPATH, self.locator.SwagInventoryPage.CONTINUE_SHOPPING)

    def verifY_cart_empty(self):
        try:
            itemsincart = BasePage.isElementPresent(self, By.XPATH, self.locator.SwagInventoryPage.ITEMS_IN_CART)
            return itemsincart
        except selenium.common.exceptions.TimeoutException as e:
            return False

    def clik_checkout_button(self):
        BasePage.click(self, By.XPATH, self.locator.SwagInventoryPage.checkout)

    def click_cancel_button(self):
        BasePage.click(self, By.XPATH, self.locator.SwagInventoryPage.cancel_button)

    def verifyCheckoutPageNavigation(self):
        return BasePage.isElementPresent(self, By.XPATH, self.locator.SwagInventoryPage.CHECKOUT_PAGE_VERIFICATION)

    def enterFirstName(self, firstName):
        BasePage.entertext(self, By.XPATH, self.locator.SwagInventoryPage.CHECKOUT_PAGE_FIRST_NAME, firstName)

    def enterLastName(self, lastName):
        BasePage.entertext(self, By.XPATH, self.locator.SwagInventoryPage.CHECKOUT_PAGE_LAST_NAME, lastName)

    def enterZip(self, zip):
        BasePage.entertext(self, By.XPATH, self.locator.SwagInventoryPage.CHECKOUT_PAGE_ZIP, zip)


    def clik_continue_button(self):
        BasePage.click(self, By.XPATH, self.locator.SwagInventoryPage.continue_button)

    def clik_all_items(self):
        BasePage.click(self, By.XPATH, self.locator.SwagInventoryPage.all_items)