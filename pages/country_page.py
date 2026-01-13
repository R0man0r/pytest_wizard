from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage
from selenium.webdriver.support.ui import WebDriverWait

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

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        return self

    def is_opened(self):
        return self.PATH in self.driver.current_url
    
    def select_country(self, country: str):
        self.wait.until(EC.element_to_be_clickable(self.COUNTRY_XPATH)).click()
        option = (By.XPATH, f"//mat-option//span[normalize-space()='{country}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()
    
    def select_timezone(self, timezone: str):
        self.wait.until(EC.element_to_be_clickable(self.TIMEZONE_XPATH)).click()
        option = (By.XPATH, f"//mat-option//span[normalize-space()='{timezone}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()

    def click_next(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()
        from .password_page import PasswordPage
        return PasswordPage(self.driver)