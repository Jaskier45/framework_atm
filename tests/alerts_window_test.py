import time

from pages.alerts_window_page import BrowserWindowPage, AlertsPage


class TestAlertFrameWindow:
    class TestBrowserWindow:
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            test_results = new_tab_page.check_opened_new_tab()
            assert test_results == 'This is a sample page', 'The new tab has not opened or an incorrect tab has opened'

        def test_new_window(self, driver):
            new_window_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            new_window_page.open()
            test_results = new_window_page.check_opened_new_window()
            assert test_results == 'This is a sample page', 'The new tab has not opened or an incorrect tab has opened'

    class TestAlertsWindow:
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button"

        def test_delay_message_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_delay_message_alert()
            assert alert_text == "This alert appeared after 5 seconds"

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            confirm_result = alert_page.check_confirm_alert()
            assert confirm_result == "You selected Ok" or confirm_result == "You selected Cancel"

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text_input, result_text = alert_page.check_prompt_alert()
            assert text_input in result_text
