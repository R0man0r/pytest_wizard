from pages.welcome_page import WelcomePage
from pages.country_page import CountryPage

def test_wizard_flow(driver):

    welcome_page = WelcomePage(driver).open()

    assert welcome_page.is_wizard_page()
    welcome_page.wait_for_title("Welcome to the Initial Setup Wizard")
    assert welcome_page.is_opened()

    country_page = welcome_page.click_start()
    country_page.wait_for_title("Choose Your Location")
    assert country_page.is_opened()

    country_page.select_country("Russia")
    country_page.select_timezone("UTC+3 Europe/Moscow")
    
    password_page = country_page.click_next()
    password_page.wait_for_title("Secure Your Device")
    assert password_page.is_opened()
    
    