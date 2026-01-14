from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class ModePage(BaseWizardPage):

    PATH = "select-desired-function"
    RADIO_ROUTER = (By.XPATH, "//input[@type='radio' and @value='router']")

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        return self
    
    
    def click_router_mode(self):
        self.driver.find_element(*self.RADIO_ROUTER).click()

    def click_next(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()
        from .mode_option_page import ModeOptionPage
        return ModeOptionPage(self.driver)
    