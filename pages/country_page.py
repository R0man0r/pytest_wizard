from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class CountryPage(BaseWizardPage):

    PATH = "select-country-or-region"

    COUNTRY_XPATH = (
        By.XPATH, 
        "//mat-label[.='Country or region']"
        "/ancestor::mat-form-field//mat-select"
    )
    TIMEZONE_XPATH = (
        By.XPATH,
        "//mat-label[normalize-space()='Time zone']"
        "/ancestor::mat-form-field//mat-select"
    )


    
    def select_country(self, country: str):
        self.wait.until(EC.element_to_be_clickable(self.COUNTRY_XPATH)).click()
        option = (By.XPATH, f"//mat-option//span[normalize-space()='{country}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()
    
    def select_timezone(self, timezone: str):
        self.wait.until(EC.element_to_be_clickable(self.TIMEZONE_XPATH)).click()
        option = (By.XPATH, f"//mat-option//span[normalize-space()='{timezone}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()

