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
