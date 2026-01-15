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
    
    def click_next(self):
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        self.driver.find_element(*self.NEXT_BUTTON).click()
        from .connection_page import ConnectionPage
        return ConnectionPage(self.driver)
    
    