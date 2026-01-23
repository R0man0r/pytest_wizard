from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class FinishSetupPage(BaseWizardPage):

    PATH = "finish"
    NEXT_BUTTON = (By.XPATH, "//button[contains(., 'Finish')]")

    
    