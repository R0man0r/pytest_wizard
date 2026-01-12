from pages.wizard_page import WizardPage

def test_wizard_welcome_page(driver):
    wizard = WizardPage(driver)

    wizard.open().wait_until_loaded()

    assert wizard.is_opened(), "Wizard welcome page is not opened as expected"