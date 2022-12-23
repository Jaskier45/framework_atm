import time
from pages.elements_page import TextBoxPage


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

