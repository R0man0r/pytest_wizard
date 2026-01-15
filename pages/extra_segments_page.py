from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_wizard_page import BaseWizardPage

class ExtraSegmentsPage(BaseWizardPage):

    PATH = "select-extra-segments"
    CHBOX_GUESTS = (By.XPATH, "//label[normalize-space()='Guests Network']")

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        return self 
    
    def click_chbox_guests(self):
        self.wait.until(EC.visibility_of_element_located(self.CHBOX_GUESTS))
        self.driver.find_element(*self.CHBOX_GUESTS).click()
    
    def click_next(self):
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BUTTON))
        self.driver.find_element(*self.NEXT_BUTTON).click()
        from .share_data_page import ShareDataPage
        return ShareDataPage(self.driver)