from selenium.webdriver.common.by import By


class TextBoxLocators:

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonLocators:
    YES = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='yesRadio']")
    Impressive = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='impressiveRadio']")
    NO = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablePageLocators:
    #add person
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRSTNAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE = (By.CSS_SELECTOR, "input[id='age']")
    SALARY = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")

    #search
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    #update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SUBMIT_AGE = (By.CSS_SELECTOR, "button[id='submit']")

    #delete
    NO_DATA = (By.CSS_SELECTOR, "div[class='rt-noData']")

    #rows_count
    SELECT_ROWS_COUNT = (By.CSS_SELECTOR, "select[aria-label='rows per page']")


class ButtonClickPage:
    DOUBLE_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME = (By.XPATH, "//button[text()='Click Me']")

    RESULT_DOUBLE_BUTTON = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RESULT_RIGHT_CLICK = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    RESULT_CLICK_ME = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinkClickPage:
    SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')


class DownloadPages:
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "a[id='downloadButton']")
    UPLOAD_FILE_BUTTON = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOAD_FILE_PATH = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")


class DynamicButtons:
    ENABLE_AFTER = (By.CSS_SELECTOR, "button[id='enableAfter']")
    COLOR_CHANGE = (By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_AFTER = (By.CSS_SELECTOR, "button[id='visibleAfter']")
