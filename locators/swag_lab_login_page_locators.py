from locators.base_page_locators import BasePageLocator


class SwagLabLoginLocator(BasePageLocator):
    LOGINBUTTON = "login-button"
    USERNAME = "user-name"
    PASSWORD = "password"
    USER_LOCK_ERROR = "//h3[contains(text(),'user has been locked out')]"

