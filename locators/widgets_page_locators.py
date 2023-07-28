from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_ITEM_TITLE = (By.CSS_SELECTOR, "div[id='section1Heading']")
    FIRST_ITEM_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")

    SECOND_ITEM_TITLE = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECOND_ITEM_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")

    THIRD_ITEM_TITLE = (By.CSS_SELECTOR, "div[id='section3Heading']")
    THIRD_ITEM_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")


class AutoCompletePageLocators:
    MULTIPLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTIPLE_VALUE = (By.CSS_SELECTOR, "div[class='css-12jo7m5 auto-complete__multi-value__label']")
    MULTIPLE_DELETE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")

    SINGLE_CONTAINER = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")


class DataPickerPageLocators:
    SELECT_DATA_BUTTON = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    SELECT_DATA_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    SELECT_DATA_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    SELECT_DATA_DAY = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    SELECT_DATA_AND_TIME = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    # SELECT_DATA_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATA_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATA_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATA_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATA_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATA_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    START_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')


class TabsPageLocators:
    WHAT_BUTTON = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    WHAT_BUTTON_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    ORIGIN_BUTTON = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    ORIGIN_BUTTON_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    USE_BUTTON = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    USE_BUTTON_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    MORE_BUTTON = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    MORE_BUTTON_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')


class TipsLocators:
    HOVER_ME_BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    HOVER_ME_TIPS = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    INPUT_FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    INPUT_TIPS = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_BUTTON = (By.XPATH, "//*[.='Contrary']")
    CONTRARY_TIPS = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    VERS_BUTTON = (By.XPATH, "//*[.='1.10.32']")
    VERS_TIPS = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")