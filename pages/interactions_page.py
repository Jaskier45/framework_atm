import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.interactions_locators import SortTableLocators, SelectableLocators
from pages.base_page import BasePage


class SortTablePage(BasePage):
    locators = SortTableLocators()

    def get_sort_elements(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.List_tab).click()
        order_before = self.get_sort_elements(self.locators.List_item)
        item_list = random.sample(self.elements_are_visible(self.locators.List_item), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sort_elements(self.locators.List_item)
        return order_before, order_after

    def change_grid_list_order(self):
        self.element_is_visible(self.locators.Grid_tab).click()
        grid_order_before = self.get_sort_elements(self.locators.Grid_item)
        item_list = random.sample(self.elements_are_visible(self.locators.Grid_item), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        grid_order_after = self.get_sort_elements(self.locators.Grid_item)
        print(grid_order_before)
        print(grid_order_after)
        return grid_order_before, grid_order_after


class SelectablePage(BasePage):
    locators = SelectableLocators()

    def click_selecteble_item(self, element):
        item_list = self.elements_are_visible(element)
        random.sample(item_list, k = 1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selecteble_item(self.locators.LIST_ITEM)
        active_elements = self.element_is_visible(self.locators.LIST_ACTIVE_ITEM)
        return active_elements.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selecteble_item(self.locators.GRID_ITEM)
        active_elements = self.element_is_visible(self.locators.GRID_ACTIVE_ITEM)
        return active_elements.text
