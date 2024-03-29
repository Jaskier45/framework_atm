import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DataPickerPage, SliderPage, ProgressBarPage, TabsPage, \
    TipsPage, MenuPage


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

    class TestSliderPage:

        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            print(before, '\n', after)
            assert before != after

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after = progress_bar.change_progress_var_value()
            print(before, '\n', after)
            assert before != after

    class TestTabsPage:

        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            # more_button, more_content = tabs.check_tabs('more')
            assert what_button == 'What' and what_content != 0
            assert origin_button == 'Origin' and origin_content != 0
            assert use_button == 'Use' and use_content != 0
            # assert more_button == 'More' and more_content != 0

    class TestToolTips:

        def test_tips(self, driver):
            tips = TipsPage(driver, 'https://demoqa.com/tool-tips')
            tips.open()
            button_text, field_text, contrary_text, section_text = tips.check_tool_tips()
            assert button_text == 'You hovered over the Button'
            assert field_text == 'You hovered over the Button'
            assert contrary_text == 'You hovered over the text field'
            assert section_text == 'You hovered over the Contrary'
            # print('\n', button_text,'\n', field_text,'\n', contrary_text,'\n', section_text)

    class TestMenuPage:

        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            exp_res = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
            data = menu_page.check_menu()
            assert data == exp_res
