from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class ConnectionPage(BaseWizardPage):

    PATH = "connect-device-to-wall-outlet"

    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    
    def click_next_when_ready(self):
        self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()
