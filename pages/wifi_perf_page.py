from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class WifiPerfPage(BaseWizardPage):

    PATH = "wifi-performance-settings"
    RADIO_OPTIMAL = (
    By.XPATH,
    "//label[.//div[contains(normalize-space(), 'Less interference')]]"
    )
    
    def click_optimal(self):
        self.wait.until(
            EC.visibility_of_element_located(self.RADIO_OPTIMAL)
            ).click()
        

    
    