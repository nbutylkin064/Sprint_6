import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By  # Добавьте эту строку
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Заполнить поле "Имя" значением "{name}"')
    def fill_name(self, name):
        self.send_keys(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполнить поле "Фамилия" значением "{surname}"')
    def fill_surname(self, surname):
        self.send_keys(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step('Заполнить поле "Адрес" значением "{address}"')
    def fill_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Выбрать станцию метро')
    def select_metro_station(self):
        self.click(OrderPageLocators.METRO_FIELD)
        self.click(OrderPageLocators.METRO_STATION)

    @allure.step('Заполнить поле "Телефон" значением "{phone}"')
    def fill_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить поле "Дата" значением "{date}"')
    def fill_date(self, date):
        self.send_keys(OrderPageLocators.DATE_FIELD, date)
        # Закрываем календарь нажатием ESC
        self.find_element(OrderPageLocators.DATE_FIELD).send_keys(Keys.ESCAPE)
        # Ожидаем скрытия календаря
        self.wait_for_element_to_disappear((By.CLASS_NAME, "react-datepicker-popper"))

    @allure.step('Выбрать срок аренды')
    def select_rental_period(self):
        # Ожидаем появления контейнера выпадающего списка
        container = self.wait_for_element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_CONTAINER)
        
        # Пробуем разные стратегии клика
        strategies = [
            lambda: container.click(),
            lambda: self.click_via_js(container),
            lambda: self.click_via_action_chains(container)
        ]
        
        success_open = False
        for strategy in strategies:
            try:
                strategy()
                # Ожидаем появления меню
                if self.is_element_visible(OrderPageLocators.RENTAL_PERIOD_MENU):
                    success_open = True
                    break
            except:
                continue
        
        if not success_open:
            # Пробуем кликнуть по плейсхолдеру
            try:
                placeholder = self.find_element(OrderPageLocators.RENTAL_PERIOD_PLACEHOLDER)
                self.click_via_js(placeholder)
            except:
                pass
        
        # Ожидаем появления опций и выбираем
        success_select = False
        
        # Список приоритетных опций для выбора
        option_locators = [
            OrderPageLocators.RENTAL_OPTION_3,  # трое суток
            OrderPageLocators.RENTAL_OPTION_2,  # двое суток  
            OrderPageLocators.RENTAL_OPTION_1,  # сутки
            OrderPageLocators.RENTAL_OPTION_4,  # четверо суток
        ]
        
        for option_locator in option_locators:
            try:
                option = self.wait_for_element_to_be_clickable(option_locator)
                self.click_via_js(option)
                success_select = True
                break
            except:
                continue
        
        # Если не нашли по тексту, пробуем найти любую опцию
        if not success_select:
            try:
                options = self.find_elements(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
                if options:
                    self.click_via_js(options[0])
                    success_select = True
            except:
                pass

    @allure.step('Выбрать цвет самоката')
    def select_scooter_color(self):
        self.click(OrderPageLocators.COLOR_BLACK)

    @allure.step('Заполнить поле "Комментарий" значением "{comment}"')
    def fill_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверить успешное создание заказа')
    def is_order_successful(self):
        return self.is_element_displayed(OrderPageLocators.SUCCESS_MESSAGE)

    @allure.step('Получить текст сообщения об успехе')
    def get_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)

    @allure.step('Заполнить первую страницу заказа')
    def fill_first_page(self, name, surname, address, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.select_metro_station()
        self.fill_phone(phone)
        self.click_next_button()

    @allure.step('Заполнить вторую страницу заказа')
    def fill_second_page(self, date, comment):
        # Ожидаем загрузки второй страницы
        self.wait_for_element_to_be_visible(OrderPageLocators.RENT_HEADER)
        
        self.fill_date(date)
        self.select_rental_period()
        self.select_scooter_color()
        self.fill_comment(comment)
        self.click_order_button()
        self.confirm_order()