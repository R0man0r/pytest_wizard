from pages import (
    WelcomePage,
    CountryPage,
    PasswordPage,
    ModePage,
    ModeOptionPage,
    SchematicPage,
    ConnectionPage,
    ScheduleUpdatesPage,
    WifiSettingsPage,
    WifiPerfPage,
    ExtraSegmentsPage,
    ShareDataPage,
    DeviceCredentialsPage,
    FinishSetupPage
)


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
    assert country_page.is_opened()
    country_page.select_country("Russia")
    # country_page.click_next_default()

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

def test_share_data_page(driver):
    share_data_page = ShareDataPage(driver).open()
    share_data_page.wait_for_title("Join the Product Improvement Programme")
    assert share_data_page.is_opened()
    share_data_page.click_not_now()

def test_device_credentials_page(driver):
    device_credentials_page = DeviceCredentialsPage(driver).open()
    device_credentials_page.wait_for_title("Store Your Keenetic Device Credentials")
    assert device_credentials_page.is_opened()
    device_credentials_page.click_next_default()

def test_finish_setup_page(driver):
    finish_setup_page = FinishSetupPage(driver).open()
    finish_setup_page.wait_for_title("Finishing the Setup")
    assert finish_setup_page.is_opened()
    finish_setup_page.click_next_default()