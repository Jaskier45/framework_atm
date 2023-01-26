from selenium.webdriver.common.by import By


class BrowserWindowPageLocator:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_TAB_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    SEE_TIME_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    ACCEPT_MESSAGE = (By.CSS_SELECTOR, "span[id='confirmResult']")
    SEE_PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_MESSAGE = (By.CSS_SELECTOR, "span[id='promptResult']")


class LocatorsFramePage:
    First_Big_iframe = (By.CSS_SELECTOR, "iframe[id='frame1']")
    Second_small_iframe = (By.CSS_SELECTOR, "iframe[id='frame2']")
    Text_frame = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFrameLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, "p")


class ModalDialogsPageLocators:
    SMALL_MODAL = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    CLOSE_SMALL_MODAL = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    TEXT_SMALL_MODAL = (By.CSS_SELECTOR, "div[class='modal-body']")
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')
    LARGE_MODAL = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    TEXT_LARGE_MODAL = (By.CSS_SELECTOR, "p")
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')
    CLOSE_LARGE_MODAL = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
