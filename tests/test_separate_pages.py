from pages.welcome_page import WelcomePage
from pages.country_page import CountryPage
from pages.password_page import PasswordPage
from pages.mode_page import ModePage
from pages.mode_option_page import ModeOptionPage




def test_welcome_page(driver):
    welcome_page = WelcomePage(driver).open()
    assert welcome_page.is_wizard_page()
    welcome_page.wait_for_title("Welcome to the Initial Setup Wizard")
    assert welcome_page.is_opened()

def test_country_page(driver):
    country_page = CountryPage(driver).open()
    assert country_page.is_wizard_page()
    country_page.wait_for_title("Choose Your Location")
    # TODO Add country and timezone selectors
    assert country_page.is_opened()

def test_password_page(driver):
    password_page = PasswordPage(driver).open()
    password_page.wait_for_title("Secure Your Device")
    assert password_page.is_opened()
    password_page.enter_password("admin1234")
    password_page.click_next_default()

def test_mode_page(driver):
    mode_page = ModePage(driver).open()
    mode_page.wait_for_title("What Would You Like to Do?")
    assert mode_page.is_opened()
    mode_page.click_router_mode()
    mode_page.click_next_default()

def test_mode_option_page(driver):
    mode_option_page = ModeOptionPage(driver).open()
    mode_option_page.wait_for_title("Choose Your Internet Connection")
    assert mode_option_page.is_opened()
    mode_option_page.click_eth_option()
    
