from locators.base_page_locators import BasePageLocator


class SwagInventoryPage(BasePageLocator):
    XPATH_PRODUCTS = "//span[text()='Products']"
    MAIN_MENU = "react-burger-menu-btn"
    LOGOUT_LINK = "logout_sidebar_link"
    CLASS_INVENTORY_FILTER_SELECT = "product_sort_container"
    CLASS_INVENTORY_PIRCE_OF_ITEMS = "//div[@class='inventory_item_price']"

