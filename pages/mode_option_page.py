from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class ModeOptionPage(BaseWizardPage):

    PATH = "select-specific-function"
    RADIO_ETH = (By.XPATH, "//input[@type='radio' and @value='via-ethernet']")

    
    def click_eth_option(self):
        self.driver.find_element(*self.RADIO_ETH).click()
    