from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage
from selenium.webdriver.support.ui import WebDriverWait

class PasswordPage(BaseWizardPage):
    PATH = "/password"

    def is_opened(self):
        return self.PATH in self.driver.current_url
    
    PASSWORD_FIELD_XPATH = "/html/body/app-root/isw-layout/mat-card/mat-card-content/isw-password/div/div/ndw-user-password-input/div/mat-form-field/div[1]"

    def enter_password(self):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PASSWORD_FIELD_XPATH))
        )
        input_field.click()
        # input_field.clear()
        input_field.send_keys("admin1234")