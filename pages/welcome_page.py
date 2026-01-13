from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class WelcomePage(BaseWizardPage):
    
    PATH = "welcome"
    START_BUTTON = (By.XPATH, "//button[contains(., 'Start')]")

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.wait.until(EC.visibility_of_element_located(self.START_BUTTON))
        return self
    
    def is_opened(self):
        return self.PATH in self.driver.current_url
    
    def click_start(self):
        self.driver.find_element(*self.START_BUTTON).click()
        from .country_page import CountryPage
        return CountryPage(self.driver)