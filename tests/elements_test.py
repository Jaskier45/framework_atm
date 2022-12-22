import time
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            page.open()
            page.fill_all_fields()
            output_name, output_email, output_cur_address, output_per_address = page.check_filled_form()
            # print(page.check_filled_form())
            print(output_name)
            print(output_email)
            print(output_cur_address)
            print(output_per_address)
            time.sleep(3)
