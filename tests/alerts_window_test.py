import time

from pages.alerts_window_page import BrowserWindowPage, AlertsPage, FramePage, NestedFramePage, ModalDialogsPage


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

    class TestFrameSwitchWindow:
        def test_frame_window(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result_frame1 = frame_page.frame_page_check('frame1')
            result_frame2 = frame_page.frame_page_check('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    class TestNestedFrames:
        def test_nested_frame(self, driver):
            nested_page = NestedFramePage(driver, "https://demoqa.com/nestedframes")
            nested_page.open()
            parent_text, child_text = nested_page.parents_child()
            assert parent_text == 'Parent frame', "The nested frame does not exist"
            assert child_text == 'Child Iframe', "The nested frame does not exist"

    class TestModalDialogs:
        def test_modal_dialogs(self, driver):
            modal_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            small, large = modal_page.check_modal_dialogs()
            assert small[1] < large[1]
            assert small[0] == 'Small Modal'
            assert large[0] == 'Large Modal'
