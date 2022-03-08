from selenium.webdriver.common.by import By
from locators import swag_lab_login_page_locators
from locators import swag_inventory_locator
from pages.base_page import BasePage


class SwagInventoryPage(BasePage):

    def __init__(self, x, filepath):
        self.driver = x
        self.filepath = filepath
        self.locator = swag_inventory_locator
        super().__init__(self.driver, self.filepath)

    def verifyInventoryPage(self):
        inventorypageverification = BasePage.isDisplayed(self, By.XPATH, self.locator.SwagInventoryPage.XPATH_PRODUCTS)
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
