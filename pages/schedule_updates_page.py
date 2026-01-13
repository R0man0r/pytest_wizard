from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class ScheduleUpdatesPage(BaseWizardPage):
    
    PATH = "auto-update-schedule"
    CHBOX_ALL_DAY = (By.XPATH, "//label[.//span[normalize-space()='All day']]")

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        return self
    
    def click_chbox_all_day(self):
        self.driver.find_element(*self.CHBOX_ALL_DAY).click()
    