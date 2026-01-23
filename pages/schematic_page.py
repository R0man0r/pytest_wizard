from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class SchematicPage(BaseWizardPage):

    PATH = "scenario-schematic"
    NEXT_BUTTON = (By.XPATH, "//button[contains(., 'Confirm')]")

    
    
    