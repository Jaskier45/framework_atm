import time

from locators.outsourcing_locators import OutsourcingPageLocators
from pages.base_page import BasePage


class OutsourcingPage(BasePage):
    locators = OutsourcingPageLocators()

    def check_logo_name(self):
        logo_name = self.element_is_visible(self.locators.logo)
        logo_text = logo_name.text
        return logo_text

    def check_phone_number(self):
        phone_number = self.element_is_visible(self.locators.phone_number)
        return phone_number.text

    def check_footer_info(self):
        footer_phone = self.element_is_visible(self.locators.footer_phone)
        footer_address = self.element_is_visible(self.locators.footer_address)
        footer_mail = self.element_is_visible(self.locators.footer_mail)
        return footer_phone.text, footer_address.text, footer_mail.text

    def check_amount_article(self):
        drop_down_menu = self.element_is_visible(self.locators.drop_down_menu)
        self.action_move_to_element(drop_down_menu)
        self.element_is_present(self.locators.yprav_konsalt).click()
        name_of_articles = self.elements_are_visible(self.locators.articles_list)
        data = []
        for item in name_of_articles:
            self.go_to_element(item)
            data.append(item.text)
        return data

    def check_amount_article_sells(self):
        drop_down_menu = self.element_is_visible(self.locators.drop_down_menu)
        self.action_move_to_element(drop_down_menu)
        self.element_is_present(self.locators.prodazhi).click()
        name_of_articles = self.elements_are_visible(self.locators.articles_list)
        data = []
        for item in name_of_articles:
            self.go_to_element(item)
            data.append(item.text)
        return data
