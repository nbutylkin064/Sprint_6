import allure
import pytest
from pages.main_page import MainPage


class TestMainPage:
    
    @allure.title('Проверка вопроса 1: "Сколько это стоит? И как оплатить?"')
    def test_faq_question_1(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.click_question(0)
        actual_answer = main_page.get_answer_text(0)
        expected_answer = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        assert actual_answer == expected_answer

    @allure.title('Проверка вопроса 2: "Хочу сразу несколько самокатов! Так можно?"')
    def test_faq_question_2(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.click_question(1)
        actual_answer = main_page.get_answer_text(1)
        expected_answer = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        assert actual_answer == expected_answer

    @allure.title('Проверка вопроса 3: "Как рассчитывается время аренды?"')
    def test_faq_question_3(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.click_question(2)
        actual_answer = main_page.get_answer_text(2)
        expected_answer = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        assert actual_answer == expected_answer

    @allure.title('Проверка вопроса 4: "Можно ли заказать самокат на сегодня?"')
    def test_faq_question_4(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.click_question(3)
        actual_answer = main_page.get_answer_text(3)
        expected_answer = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        assert actual_answer == expected_answer

    @allure.title('Проверка вопроса 5: "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_faq_question_5(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.click_question(4)
        actual_answer = main_page.get_answer_text(4)
        expected_answer = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        assert actual_answer == expected_answer

    @allure.title('Проверка вопроса 6: "Вы привозите зарядку вместе с самокатом?"')
    def test_faq_question_6(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.click_question(5)
        actual_answer = main_page.get_answer_text(5)
        expected_answer = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        assert actual_answer == expected_answer

    @allure.title('Проверка вопроса 7: "Можно ли отменить заказ?"')
    def test_faq_question_7(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.click_question(6)
        actual_answer = main_page.get_answer_text(6)
        expected_answer = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        assert actual_answer == expected_answer

    @allure.title('Проверка вопроса 8: "Я жизу за МКАДом, привезёте?"')
    def test_faq_question_8(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.click_question(7)
        actual_answer = main_page.get_answer_text(7)
        expected_answer = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        assert actual_answer == expected_answer