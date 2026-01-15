from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class WifiPerfPage(BaseWizardPage):

    PATH = "wifi-performance-settings"
    RADIO_OPTIMAL = (
    By.XPATH,
    "//label[.//div[contains(normalize-space(), 'Less interference')]]"
    )

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        return self 
    
    def click_optimal(self):
        self.wait.until(
            EC.visibility_of_element_located(self.RADIO_OPTIMAL)
            ).click()
        

    def click_next(self):
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        self.driver.find_element(*self.NEXT_BUTTON).click()
        from .extra_segments_page import ExtraSegmentsPage
        return ExtraSegmentsPage(self.driver)
    
    