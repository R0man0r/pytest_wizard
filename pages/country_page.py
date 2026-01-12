from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage
from selenium.webdriver.support.ui import WebDriverWait

class CountryPage(BaseWizardPage):

    PATH = "/select-country-or-region"
    NEXT_BUTTON = (By.XPATH, "//button[contains(., 'Next')]")

    COUNTRY_XPATH = "/html/body/app-root/isw-layout/mat-card/mat-card-content/isw-select-country-or-region/div/form/ndw-select[1]/div/mat-form-field"
    TIMEZONE_XPATH = "/html/body/app-root/isw-layout/mat-card/mat-card-content/isw-select-country-or-region/div/form/ndw-select[2]/div/mat-form-field"

    def is_opened(self):
        return self.PATH in self.driver.current_url
    
    def select_country(self, country_name: str):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COUNTRY_XPATH)))
        dropdown.click()
        WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//mat-option//span[contains(., '{country_name}')]"))
    )
        country_option = (By.XPATH, f"//mat-option//span[contains(., '{country_name}')]")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(country_option)).click()
    
    def select_timezone(self, timezone_name: str):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.TIMEZONE_XPATH)))
        dropdown.click()
        WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//mat-option//span[contains(., '{timezone_name}')]"))
    )
        timezone_option = (By.XPATH, f"//mat-option//span[contains(., '{timezone_name}')]")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(timezone_option)).click()

    def click_next(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()
        from .password_page import PasswordPage
        return PasswordPage(self.driver)