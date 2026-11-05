"""Testes E2E mobile (Android) dirigindo o app Configurações via Appium."""
from appium.webdriver.common.appiumby import AppiumBy


def test_settings_app_launches(driver):
    assert "settings" in driver.current_package.lower()


def test_settings_shows_menu_items(driver):
    items = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    assert len(items) > 0, "nenhum item de menu encontrado no app Configurações"


def test_can_scroll_settings(driver):
    size = driver.get_window_size()
    driver.execute_script(
        "mobile: scrollGesture",
        {
            "left": int(size["width"] * 0.1),
            "top": int(size["height"] * 0.2),
            "width": int(size["width"] * 0.8),
            "height": int(size["height"] * 0.6),
            "direction": "down",
            "percent": 1.0,
        },
    )
    assert "settings" in driver.current_package.lower()
