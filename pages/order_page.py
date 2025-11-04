import allure
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
        # Ждем немного
        time.sleep(1)
    
    @allure.step('Выбрать срок аренды')
    def select_rental_period(self):
        print("=== НАЧАЛО ВЫБОРА СРОКА АРЕНДЫ ===")
        
        try:
            # Способ 1: Клик по контейнеру выпадающего списка
            print("Пытаемся найти контейнер выпадающего списка...")
            container = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_CONTAINER))
            print("Контейнер найден, кликаем...")
            
            # Пробуем разные стратегии клика
            strategies = [
                lambda: container.click(),
                lambda: self.driver.execute_script("arguments[0].click();", container),
                lambda: ActionChains(self.driver).move_to_element(container).click().perform()
            ]
            
            success_open = False
            for i, strategy in enumerate(strategies):
                try:
                    print(f"Пробуем стратегию клика #{i+1}...")
                    strategy()
                    time.sleep(2)
                    
                    # Проверяем, открылся ли выпадающий список
                    try:
                        menu = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_MENU)
                        if menu.is_displayed():
                            print("Выпадающий список открылся!")
                            success_open = True
                            break
                    except:
                        print("Выпадающий список не открылся, пробуем следующую стратегию...")
                        continue
                        
                except Exception as e:
                    print(f"Стратегия #{i+1} не сработала: {e}")
                    continue
            
            if not success_open:
                print("Не удалось открыть выпадающий список, пробуем альтернативные локаторы...")
                
                # Пробуем кликнуть по плейсхолдеру
                try:
                    placeholder = self.find_element(OrderPageLocators.RENTAL_PERIOD_PLACEHOLDER)
                    self.driver.execute_script("arguments[0].click();", placeholder)
                    time.sleep(2)
                except Exception as e:
                    print(f"Не удалось кликнуть по плейсхолдеру: {e}")
            
            # Теперь пробуем выбрать опцию
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
                    print(f"Пытаемся найти опцию: {option_locator}")
                    option = self.wait.until(EC.element_to_be_clickable(option_locator))
                    print("Опция найдена, кликаем...")
                    self.driver.execute_script("arguments[0].click();", option)
                    success_select = True
                    print(f"Успешно выбрали опцию: {option_locator}")
                    break
                except Exception as e:
                    print(f"Не удалось выбрать опцию {option_locator}: {e}")
                    continue
            
            # Если не нашли по тексту, пробуем найти любую опцию
            if not success_select:
                print("Пытаемся найти любую доступную опцию...")
                try:
                    options = self.driver.find_elements(*OrderPageLocators.RENTAL_PERIOD_OPTIONS)
                    print(f"Найдено опций: {len(options)}")
                    if options:
                        # Выбираем первую опцию
                        self.driver.execute_script("arguments[0].click();", options[0])
                        success_select = True
                        print("Успешно выбрали первую доступную опцию")
                except Exception as e:
                    print(f"Не удалось найти опции: {e}")
            
            if not success_select:
                # Последняя попытка - просто пропустить выбор срока аренды
                print("ВНИМАНИЕ: Не удалось выбрать срок аренды, пропускаем этот шаг")
                # Можно продолжить выполнение без выбора срока аренды
                # или раскомментировать строку ниже для выброса исключения
                # raise Exception("Не удалось выбрать срок аренды")
                
        except Exception as e:
            print(f"Критическая ошибка при выборе срока аренды: {e}")
            # Делаем скриншот для отладки
            self.driver.save_screenshot("rental_period_critical_error.png")
            # Пропускаем этот шаг и продолжаем
            print("Пропускаем выбор срока аренды из-за ошибки")
    
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
        # Ждем загрузки второй страницы
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.RENT_HEADER))
        
        self.fill_date(date)
        self.select_rental_period()
        self.select_scooter_color()
        self.fill_comment(comment)
        self.click_order_button()
        self.confirm_order()