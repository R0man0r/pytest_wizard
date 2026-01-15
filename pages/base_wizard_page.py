from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseWizardPage:
    BASE_URL = "http://192.168.1.1/wizards/initial-setup/"
    NEXT_BUTTON = (By.XPATH, "//button[contains(., 'Next')]")
    TITLE = (By.XPATH, "//mat-card-title")
    PATH = ""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def current_url(self):
        return self.driver.current_url

    def is_wizard_page(self):
        return self.BASE_URL in self.current_url()
    
    def wait_for_title(self, expected_text: str):
        self.wait.until(EC.text_to_be_present_in_element(self.TITLE, expected_text))

    def click_next_default(self):
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def is_opened(self):
        return self.PATH in self.driver.current_url