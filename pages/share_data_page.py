from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class ShareDataPage(BaseWizardPage):

    PATH = "product-improvement"
    BTN_NOT_NOW = (By.XPATH, "//button[contains(., 'Not now')]")
    NEXT_BUTTON = (By.XPATH, "//button[contains(., 'Join')]")

    
    def click_not_now(self):
        self.driver.find_element(*self.BTN_NOT_NOW).click()
