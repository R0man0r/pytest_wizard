from pages.welcome_page import WelcomePage
from pages.country_page import CountryPage
from pages.password_page import PasswordPage
from pages.mode_page import ModePage
from pages.mode_option_page import ModeOptionPage
from pages.schematic_page import SchematicPage
from pages.connection_page import ConnectionPage
from pages.schedule_updates_page import ScheduleUpdatesPage
from pages.wifi_settings_page import WifiSettingsPage
from pages.wifi_perf_page import WifiPerfPage
from pages.extra_segments_page import ExtraSegmentsPage


def test_welcome_page(driver):
    welcome_page = WelcomePage(driver).open()
    assert welcome_page.is_wizard_page()
    welcome_page.wait_for_title("Welcome to the Initial Setup Wizard")
    assert welcome_page.is_opened()
    welcome_page.click_next_default()

def test_country_page(driver):
    country_page = CountryPage(driver).open()
    assert country_page.is_wizard_page()
    country_page.wait_for_title("Choose Your Location")
    # TODO Add country and timezone selectors
    assert country_page.is_opened()
    country_page.click_next_default()

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
    mode_option_page.click_next_default()
    
def test_schematic_page(driver):
    schematic_page = SchematicPage(driver).open()
    schematic_page.wait_for_title("Confirm Your Internet Connection")
    assert schematic_page.is_opened()
    schematic_page.click_next_default()

def test_connection_page(driver):
    connection_page = ConnectionPage(driver).open()
    connection_page.wait_for_title("Connect to Your Provider’s Ethernet")
    assert connection_page.is_opened()
    connection_page.click_next_when_ready()

def test_schedule_updates_page(driver):
    schedule_updates_page = ScheduleUpdatesPage(driver).open()
    schedule_updates_page.wait_for_title("Schedule Automatic Software Updates")
    assert schedule_updates_page.is_opened()
    schedule_updates_page.click_chbox_all_day()
    schedule_updates_page.click_next_default()

def test_wifi_settings_page(driver):
    wifi_settings_page = WifiSettingsPage(driver).open()
    wifi_settings_page.wait_for_title("Wi-Fi Network Settings")
    assert wifi_settings_page.is_opened()

def test_wifi_perf_page(driver):
    wifi_perf_page = WifiPerfPage(driver).open()
    wifi_perf_page.wait_for_title("Optimize Wi-Fi Network Performance")
    assert wifi_perf_page.is_opened()
    wifi_perf_page.click_optimal()

def test_extra_segments_page(driver):
    extra_segments_page = ExtraSegmentsPage(driver).open()
    extra_segments_page.wait_for_title("Create Additional Wi-Fi Networks")
    assert extra_segments_page.is_opened()
    extra_segments_page.click_chbox_guests()