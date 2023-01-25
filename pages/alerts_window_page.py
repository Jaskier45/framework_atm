import random
import time

from locators.alerts_window_locators import BrowserWindowPageLocator, AlertsPageLocators, LocatorsFramePage, \
    NestedFrameLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowPageLocator()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_TEXT).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_TEXT).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_delay_message_alert(self):
        self.element_is_visible(self.locators.SEE_TIME_ALERT_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):
        result = random.randint(0, 1)
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        if result == 0:
            alert_window.accept()
        else:
            alert_window.dismiss()
        text_result = self.element_is_present(self.locators.ACCEPT_MESSAGE).text
        return text_result

    def check_prompt_alert(self):
        text = f'autotest{random.randint(0,999)}'
        self.element_is_visible(self.locators.SEE_PROMPT_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        result_text = self.element_is_present(self.locators.PROMPT_MESSAGE).text
        return text, result_text


class FramePage(BasePage):
    locators = LocatorsFramePage()

    def frame_page_check(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.First_Big_iframe)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.Text_frame).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.Second_small_iframe)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.Text_frame).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramePage(BasePage):
    locators = NestedFrameLocators()

    def parents_child(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text
