import random
from selenium.webdriver.common.by import By


class OutsourcingPageLocators:
    logo = (By.CSS_SELECTOR, 'h1[itemprop="name"]')
    phone_number = (By.CSS_SELECTOR, 'div[data-id="929de48"]')
    footer_phone = (By.CSS_SELECTOR, 'li[id="menu-item-494"]')
    footer_address = (By.CSS_SELECTOR, 'li[id="menu-item-895"]')
    footer_mail = (By.CSS_SELECTOR, 'li[id="menu-item-495"]')
    drop_down_menu = (By.CSS_SELECTOR, 'li[id="menu-item-774"]')
    yprav_konsalt = (By.CSS_SELECTOR, 'li[id="menu-item-890"]')
    prodazhi = (By.CSS_SELECTOR, 'li[id="menu-item-889"]')
    articles_list = (By.CSS_SELECTOR, "h2[class='elementor-heading-title elementor-size-default']")
