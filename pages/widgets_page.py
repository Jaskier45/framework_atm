from selenium.common import TimeoutException

from locators.widgets_page_locators import AccordianPageLocators
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
