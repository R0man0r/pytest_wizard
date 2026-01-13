from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class WifiSettingsPage(BaseWizardPage):

    PATH = "wifi-settings"

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        return self 
    
    