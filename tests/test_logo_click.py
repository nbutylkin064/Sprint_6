import allure
from pages.main_page import MainPage
from data import TestData


class TestLogoClick:
    @allure.title('Проверка перехода на главную страницу по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Перейти на страницу заказа'):
            main_page.click_order_button_header()
        
        with allure.step('Кликнуть на логотип Самоката'):
            main_page.click_scooter_logo()
        
        with allure.step('Проверить переход на главную страницу'):
            assert main_page.is_main_page_loaded(), "Не произошел переход на главную страницу"
            current_url = main_page.get_current_url()
            assert current_url == TestData.BASE_URL, \
                f"Ожидался URL: {TestData.BASE_URL}, но получен: {current_url}"

    @allure.title('Проверка перехода на Дзен по логотипу Яндекса')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Кликнуть на логотип Яндекса'):
            main_page.click_yandex_logo()
        
        with allure.step('Переключиться на новую вкладку'):
            main_page.switch_to_new_tab()
            main_page.wait_for_page_load()
        
        with allure.step('Проверить переход на Дзен'):
            current_url = main_page.get_current_url()
            assert 'dzen.ru' in current_url, \
                f"Ожидался переход на Дзен, но текущий URL: {current_url}"