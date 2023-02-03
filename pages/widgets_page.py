import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DataPickerPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {
                     'first':
                         {
                             'title': self.locators.FIRST_ITEM_TITLE,
                             'content': self.locators.FIRST_ITEM_CONTENT
                         },
                     'second':
                         {
                             'title': self.locators.SECOND_ITEM_TITLE,
                             'content': self.locators.SECOND_ITEM_CONTENT
                         },
                     'third':
                         {
                             'title': self.locators.THIRD_ITEM_TITLE,
                             'content': self.locators.THIRD_ITEM_CONTENT
                         }
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTIPLE_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTIPLE_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTIPLE_DELETE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTIPLE_VALUE))
        return count_value_before, count_value_after

    def check_color_multi(self):
        color_list = self.elements_are_present(self.locators.MULTIPLE_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_single_input(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_single_field(self):
        color_result = self.element_is_visible(self.locators.SINGLE_CONTAINER)
        return color_result.text


class DataPickerPage(BasePage):
    locators = DataPickerPageLocators()

    def set_date(self):
        data = next(generated_date())
        input_date = self.element_is_visible(self.locators.SELECT_DATA_BUTTON)
        value_data_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.SELECT_DATA_MONTH, data.month)
        self.set_date_by_text(self.locators.SELECT_DATA_YEAR, data.year)
        self.set_date_item_from_list(self.locators.SELECT_DATA_DAY, data.day)
        value_data_after = input_date.get_attribute('value')
        return value_data_before, value_data_after

    def select_date_and_time(self):
        data = next(generated_date())
        input_date = self.element_is_visible(self.locators.SELECT_DATA_AND_TIME)
        value_data_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATA_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATA_AND_TIME_MONTH_LIST, data.month)
        self.element_is_visible(self.locators.DATA_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATA_AND_TIME_YEAR_LIST, data.year)
        self.set_date_item_from_list(self.locators.SELECT_DATA_DAY, data.day)
        self.set_date_item_from_list(self.locators.DATA_AND_TIME_TIME_LIST, data.time)
        input_date_after = self.element_is_visible(self.locators.SELECT_DATA_AND_TIME)
        value_data_after = input_date_after.get_attribute('value')
        return value_data_before, value_data_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

