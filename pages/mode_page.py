from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class ModePage(BaseWizardPage):

    PATH = "select-desired-function"
    RADIO_ROUTER_LABEL = (
    By.XPATH,
    "//label[.//div[contains(normalize-space(), 'Router Mode')]]"
    )

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        return self
    
    
    def click_router_mode(self):
        self.wait.until(
        EC.visibility_of_element_located(self.RADIO_ROUTER_LABEL)
        ).click()
