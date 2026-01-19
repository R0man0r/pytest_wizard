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


def test_wizard_flow(driver):
    welcome_page = WelcomePage(driver).open()
    assert welcome_page.is_wizard_page()
    welcome_page.wait_for_title("Welcome to the Initial Setup Wizard")
    assert welcome_page.is_opened()
    welcome_page.click_next_default()

    country_page = CountryPage(driver)
    country_page.wait_for_title("Choose Your Location")
    # country_page.select_country("Russia")
    assert country_page.is_opened()
    country_page.click_next_default()

    password_page = PasswordPage(driver)
    password_page.wait_for_title("Secure Your Device")
    assert password_page.is_opened()
    password_page.enter_password("admin1234")
    password_page.click_next_default()

    mode_page = ModePage(driver)
    mode_page.wait_for_title("What Would You Like to Do?")
    assert mode_page.is_opened()
    mode_page.click_router_mode()
    mode_page.click_next_default()

    mode_option_page = ModeOptionPage(driver)
    mode_option_page.wait_for_title("Choose Your Internet Connection")
    assert mode_option_page.is_opened()
    mode_option_page.click_eth_option()
    mode_option_page.click_next_default()
    
    schematic_page = SchematicPage(driver)
    schematic_page.wait_for_title("Confirm Your Internet Connection")
    assert schematic_page.is_opened()
    schematic_page.click_next_default()

    connection_page = ConnectionPage(driver)
    connection_page.wait_for_title("Connect to Your Provider’s Ethernet")
    assert connection_page.is_opened()
    connection_page.click_next_when_ready()

    schedule_updates_page = ScheduleUpdatesPage(driver)
    schedule_updates_page.wait_for_title("Schedule Automatic Software Updates")
    assert schedule_updates_page.is_opened()
    schedule_updates_page.click_chbox_all_day()
    schedule_updates_page.click_next_default()

    wifi_settings_page = WifiSettingsPage(driver)
    wifi_settings_page.wait_for_title("Wi-Fi Network Settings")
    assert wifi_settings_page.is_opened()
    wifi_settings_page.click_next_default()

    wifi_perf_page = WifiPerfPage(driver)
    wifi_perf_page.wait_for_title("Optimize Wi-Fi Network Performance")
    assert wifi_perf_page.is_opened()
    wifi_perf_page.click_optimal()
    wifi_perf_page.click_next_default()

    extra_segments_page = ExtraSegmentsPage(driver)
    extra_segments_page.wait_for_title("Create Additional Wi-Fi Networks")
    assert extra_segments_page.is_opened()
    extra_segments_page.click_chbox_guests()
    extra_segments_page.click_next_default()

    share_data_page = ShareDataPage(driver)
    share_data_page.wait_for_title("Join the Product Improvement Programme")
    assert share_data_page.is_opened()
    share_data_page.click_not_now()
    share_data_page.click_next_default()

    device_credentials_page = DeviceCredentialsPage(driver)
    device_credentials_page.wait_for_title("Store Your Keenetic Device Credentials")
    assert device_credentials_page.is_opened()
    device_credentials_page.click_next_default()

    finish_setup_page = FinishSetupPage(driver)
    finish_setup_page.wait_for_title("Finishing the Setup")
    assert finish_setup_page.is_opened()
    finish_setup_page.click_next_default()