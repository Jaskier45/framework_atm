import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.interactions_locators import SortTableLocators, SelectableLocators, ResizablePageLocators
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


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_min_max_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_min_max_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_px_from_width_height(self.get_min_max_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 50), random.randint(1, 50))
        max_size = self.get_px_from_width_height(self.get_min_max_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, 1), random.randint(-200, 1))
        min_size = self.get_px_from_width_height(self.get_min_max_size(self.locators.RESIZABLE))
        return max_size, min_size
