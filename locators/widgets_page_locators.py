from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_ITEM_TITLE = (By.CSS_SELECTOR, "div[id='section1Heading']")
    FIRST_ITEM_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")

    SECOND_ITEM_TITLE = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECOND_ITEM_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")

    THIRD_ITEM_TITLE = (By.CSS_SELECTOR, "div[id='section3Heading']")
    THIRD_ITEM_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")
