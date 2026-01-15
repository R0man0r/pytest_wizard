from pages.welcome_page import WelcomePage

def test_wizard_flow(driver):

    welcome_page = WelcomePage(driver).open()

    assert welcome_page.is_wizard_page()
    welcome_page.wait_for_title("Welcome to the Initial Setup Wizard")
    assert welcome_page.is_opened()

    country_page = welcome_page.click_start()
    country_page.wait_for_title("Choose Your Location")
    assert country_page.is_opened()
    
    password_page = country_page.click_next()
    password_page.wait_for_title("Secure Your Device")
    assert password_page.is_opened()
    password_page.enter_password("admin1234")

    mode_page = password_page.click_next()
    mode_page.wait_for_title("What Would You Like to Do?")
    assert mode_page.is_opened()
    mode_page.click_router_mode()
    
    mode_option_page = mode_page.click_next()
    mode_option_page.wait_for_title("Choose Your Internet Connection")
    assert mode_option_page.is_opened()
    mode_option_page.click_eth_option()

    schematic_page = mode_option_page.click_next()
    schematic_page.wait_for_title("Confirm Your Internet Connection")
    assert schematic_page.is_opened()
    
    connection_page = schematic_page.click_next()
    connection_page.wait_for_title("Connect to Your Provider’s Ethernet")
    assert connection_page.is_opened()

    schedule_updates_page = connection_page.click_next()
    schedule_updates_page.wait_for_title("Schedule Automatic Software Updates")
    assert schedule_updates_page.is_opened()
    schedule_updates_page.click_chbox_all_day()

    wifi_settings_page = schedule_updates_page.click_next()
    wifi_settings_page.wait_for_title("Wi-Fi Network Settings")
    assert wifi_settings_page.is_opened()

    wifi_perf_page = wifi_settings_page.click_next()
    wifi_perf_page.wait_for_title("Optimize Wi-Fi Network Performance")
    assert wifi_perf_page.is_opened()
    wifi_perf_page.click_optimal()

    extra_segments_page = wifi_perf_page.click_next()
    extra_segments_page.wait_for_title("Create Additional Wi-Fi Networks")
    assert extra_segments_page.is_opened()
    extra_segments_page.click_chbox_guests()

    share_data_page = extra_segments_page.click_next()
    share_data_page.wait_for_title("Join the Product Improvement Programme")
    assert share_data_page.is_opened()

    device_credentials_page = share_data_page.click_next()
    device_credentials_page.wait_for_title("Store Your Keenetic Device Credentials")
    assert device_credentials_page.is_opened()

    finish_setup_page = device_credentials_page.click_next()
    finish_setup_page.wait_for_title("Finishing the Setup")
    assert finish_setup_page.is_opened()
    finish_setup_page.click_next_default()
    
    