import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APPIUM_SERVER = os.getenv("APPIUM_SERVER", "http://127.0.0.1:4723")


@pytest.fixture
def driver():
    """Opens the Android Settings app — a built-in app that exists on every
    device/emulator, so the suite needs no external APK to run."""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.android.settings"
    options.app_activity = ".Settings"
    options.auto_grant_permissions = True
    options.new_command_timeout = 120

    driver = webdriver.Remote(APPIUM_SERVER, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
