from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class ModeOptionPage(BaseWizardPage):

    PATH = "select-specific-function"
    RADIO_ETH = (By.XPATH, "//input[@type='radio' and @value='via-ethernet']")

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        return self
    
    def click_eth_option(self):
        self.driver.find_element(*self.RADIO_ETH).click()
    
    def click_next(self):
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        self.driver.find_element(*self.NEXT_BUTTON).click()
        from .schematic_page import SchematicPage
        return SchematicPage(self.driver)