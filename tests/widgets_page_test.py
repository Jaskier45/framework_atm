import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DataPickerPage


class TestWidgets:
    class TestAccordionPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

    class TestAutoCompletePage:
        def test_multi_auto(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_multi()
            assert colors == colors_result

        def test_delete_multi_auto(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before > count_value_after

        def test_single_add_color(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_single_input()
            color_result = autocomplete_page.check_single_field()
            assert color == color_result

    class TestDataPickerPage:

        def test_change_data(self, driver):
            data_picker_page = DataPickerPage(driver, "https://demoqa.com/date-picker")
            data_picker_page.open()
            value_data_before, value_data_after = data_picker_page.set_date()
            assert value_data_before != value_data_after

        def test_change_data_and_time(self, driver):
            data_picker_page = DataPickerPage(driver, "https://demoqa.com/date-picker")
            data_picker_page.open()
            value_data_before, value_data_after = data_picker_page.select_date_and_time()
            print(value_data_before, value_data_after)
            assert value_data_before != value_data_after
        #
