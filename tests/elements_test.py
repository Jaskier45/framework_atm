import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            page.open()
            # don't detail check
            # input_data = page.fill_all_fields()
            # output_data = page.check_filled_form()
            full_name, email, current_address, permanent_address = page.fill_all_fields()
            output_name, output_email, output_cur_address, output_per_address = page.check_filled_form()
            # print(page.check_filled_form())
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_address, "the current address does not match"
            assert permanent_address == output_per_address, "the permanent address does not match"
            time.sleep(3)

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox, 'checkboxes have not been selected'
            time.sleep(5)

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_results()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_results()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_results()
            assert output_yes == 'Yes'
            assert output_impressive == 'Impressive'
            assert output_no == 'No'
