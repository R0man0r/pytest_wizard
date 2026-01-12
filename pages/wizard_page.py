from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WizardPage:
    URL = "http://192.168.1.1/wizards/initial-setup/welcome"

    # Locators
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Welcome')]")
    START_BUTTON = (By.XPATH, "//button[contains(., 'Start setup')]")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
        return self

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.START_BUTTON))
        return self
    
    def is_opened(self) -> bool:
        return (
            self.driver.current_url.startswith(self.URL)
            and self.driver.find_element(*self.START_BUTTON).is_displayed()
        )

