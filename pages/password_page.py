from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage
from selenium.webdriver.support.ui import WebDriverWait

class PasswordPage(BaseWizardPage):
    
    PATH = "password"

    
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")

    def enter_password(self, password: str):
        field = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_FIELD)
        )
        field.clear()
        field.send_keys(password)
        return self
    
        