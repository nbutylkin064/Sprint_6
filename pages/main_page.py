import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    
    @allure.step('Прокрутить к разделу "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)
    
    @allure.step('Кликнуть на вопрос номер {question_num}')
    def click_question(self, question_num):
        self.click(MainPageLocators.FAQ_QUESTIONS[question_num])
    
    @allure.step('Получить текст ответа на вопрос номер {question_num}')
    def get_answer_text(self, question_num):
        return self.get_text(MainPageLocators.FAQ_ANSWERS[question_num])
    
    @allure.step('Кликнуть на кнопку "Заказать" в хедере')
    def click_order_button_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)
    
    @allure.step('Кликнуть на кнопку "Заказать" в основной части')
    def click_order_button_main(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MAIN)
        self.click(MainPageLocators.ORDER_BUTTON_MAIN)
    
    @allure.step('Кликнуть на логотип Самоката')
    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)
    
    @allure.step('Кликнуть на логотип Яндекса')
    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)
    
    @allure.step('Проверить, что главная страница загружена')
    def is_main_page_loaded(self):
        return self.is_element_displayed(MainPageLocators.MAIN_HEADER)
    
    @allure.step('Получить текст главного заголовка')
    def get_main_header_text(self):
        return self.get_text(MainPageLocators.MAIN_HEADER)