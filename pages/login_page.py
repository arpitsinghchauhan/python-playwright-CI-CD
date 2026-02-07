from core.base_page import BasePage
from core.config import Config

class LoginPage(BasePage):
    #Page object for sauce demo login page
    #selctors are kept private to this class
    #selectors
    _USER_NAME_INPUT = "#user-name"
    _PASSWORD_INPUT = "#password"
    _LOGIN_BUTTON = "#login-button"
    _ERROR_MSG = "[data-test='error']"
    _INVENTORY_CONTAINER = "#inventory_container"

    def login(self,username:str,password:str):
        #Method to perform login action
        self.navigate(Config.BASE_URL_UI)
        self.fill_text(self._USER_NAME_INPUT,username)
        self.fill_text(self._PASSWORD_INPUT,password)
        self.click(self._LOGIN_BUTTON)

    def is_inventory_visible(self) -> bool:
        #Method to check if inventory page is visible
        return self.is_element_visible(self._INVENTORY_CONTAINER)   

    def get_error_message(self) -> str:
        #Method to fetch error message on failed login
       return self.get_text(self._ERROR_MSG)