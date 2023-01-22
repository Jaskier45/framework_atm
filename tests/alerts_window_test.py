import time

from pages.alerts_window_page import BrowserWindowPage


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
