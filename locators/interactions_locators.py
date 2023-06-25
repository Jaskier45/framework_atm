import random

from selenium.webdriver.common.by import By


class SortTableLocators:
    List_tab = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    List_item = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

    Grid_tab = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    Grid_item = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')
