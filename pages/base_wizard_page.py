from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseWizardPage:
    BASE_URL = "http://192.168.1.1/wizards/initial-setup/"

    TITLE = (By.XPATH, "//mat-card-title")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def current_url(self):
        return self.driver.current_url

    def is_wizard_page(self):
        return self.BASE_URL in self.current_url()
    
    def wait_for_title(self, expected_text: str):
        self.wait.until(EC.text_to_be_present_in_element(self.TITLE, expected_text))