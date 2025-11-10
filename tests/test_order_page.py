import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData


class TestOrderPage:
    
    @allure.title('Проверка оформления заказа через кнопку в хедере')
    def test_order_via_header_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_order_button_header()
        order_page.fill_first_page(
            TestData.ORDER_DATA_1['name'],
            TestData.ORDER_DATA_1['surname'], 
            TestData.ORDER_DATA_1['address'],
            TestData.ORDER_DATA_1['phone']
        )
        
        order_page.fill_second_page(
            TestData.ORDER_DATA_1['date'],
            TestData.ORDER_DATA_1['comment']
        )
        
        assert order_page.is_order_successful(), "Заказ не был создан успешно"
        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message

    @allure.title('Проверка оформления заказа через кнопку внизу страницы')
    def test_order_via_main_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_order_button_main()
        order_page.fill_first_page(
            TestData.ORDER_DATA_2['name'],
            TestData.ORDER_DATA_2['surname'], 
            TestData.ORDER_DATA_2['address'],
            TestData.ORDER_DATA_2['phone']
        )
        
        order_page.fill_second_page(
            TestData.ORDER_DATA_2['date'],
            TestData.ORDER_DATA_2['comment']
        )
        
        assert order_page.is_order_successful(), "Заказ не был создан успешно"
        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message