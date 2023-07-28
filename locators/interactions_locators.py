import random

from selenium.webdriver.common.by import By


class SortTableLocators:
    List_tab = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    List_item = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

    Grid_tab = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    Grid_item = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectableLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ACTIVE_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_ACTIVE_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')
