from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class SchematicPage(BaseWizardPage):

    PATH = "scenario-schematic"
    NEXT_BUTTON = (By.XPATH, "//button[contains(., 'Confirm')]")

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        return self 
    
    def is_opened(self):
        return self.PATH in self.driver.current_url
    