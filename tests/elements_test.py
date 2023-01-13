import random
import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage


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

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            keyword = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_people(keyword)
            table_result = web_table_page.check_search_person()
            print(keyword)
            print(table_result)
            assert keyword in table_result

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_people(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            print(age)
            print(row)
            assert age in row, "The person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_people(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted_button()
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            print(count)
            assert count == [5, 10, 20, 25, 50, 100], 'The row count is not displayed in the users table list'

    class TestButtonPage:
        def test_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_button('double')
            right = button_page.click_button('right')
            click = button_page.click_button('click')
            # print(double)
            # print(right)
            # print(click)
            assert double == 'You have done a double click'
            assert right == 'You have done a right click'
            assert click == 'You have done a dynamic click'

    class TestLinksPage:
        def test_check_link(self, driver):
            link_page = LinksPage(driver, 'https://demoqa.com/links')
            link_page.open()
            href_link, current_link = link_page.check_new_tab_simple_link()
            assert href_link == current_link

        def test_broken_link(self, driver):
            link_page = LinksPage(driver, 'https://demoqa.com/links')
            link_page.open()
            response_code = link_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400
