from pages.outsourcing_page import OutsourcingPage


class TestOutsourcingForm:
    class TestOutsourcingTestPage:
        def test_logo(self, driver):
            outsourcing_page = OutsourcingPage(driver, 'https://outsourcing.ankhora.co.uk/')
            outsourcing_page.open()
            logo_text = outsourcing_page.check_logo_name()
            assert logo_text == 'OUTSOURCING'

        def test_phone_number(self, driver):
            outsourcing_page = OutsourcingPage(driver, 'https://outsourcing.ankhora.co.uk/')
            outsourcing_page.open()
            phone_number = outsourcing_page.check_phone_number()
            assert phone_number == '+4 479 356 614 95'

        def test_footer_info(self, driver):
            outsourcing_page = OutsourcingPage(driver, 'https://outsourcing.ankhora.co.uk/')
            outsourcing_page.open()
            footer_phone, footer_address, footer_mail = outsourcing_page.check_footer_info()
            assert footer_phone == '+4 479 356 614 95'
            assert footer_address == '5 High St, Maidenhead SL6 1JN, UK'
            assert footer_mail == 'business@outsourcing.ankhora.co.uk'

        def test_amount_of_articles(self, driver):
            outsourcing_page = OutsourcingPage(driver, 'https://outsourcing.ankhora.co.uk/')
            outsourcing_page.open()
            expected_result = ['Розробка стратегій розвитку компанії', 'Корпоративна діагностика', 'Оптимізація бізнес-процесів', 'Розробка бізнес плану та оцінка компанії', 'Супровід при виході на ринок', 'Розробка моделі управлінської звітності']
            actual_result = outsourcing_page.check_amount_article()
            assert actual_result == expected_result

        def test_amount_of_articles_sells(self, driver):
            outsourcing_page = OutsourcingPage(driver, 'https://outsourcing.ankhora.co.uk/')
            outsourcing_page.open()
            expected_result = ['Технології та програмне забезпечення', 'E-commerce', 'Продажі в соціальних мережах', 'Франчайзинг', 'Телемаркетинг']
            actual_result = outsourcing_page.check_amount_article_sells()
            assert actual_result == expected_result
