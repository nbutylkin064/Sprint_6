import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Увеличили время ожидания до 20 секунд
    
    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Найти элементы')
    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    @allure.step('Кликнуть на элемент')
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        # Пробуем обычный клик, если не получается - используем JavaScript
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step('Ввести текст "{text}" в поле')
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step('Скроллить к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Проверить, что элемент отображается')
    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    @allure.step('Получить значение атрибута "{attribute}" элемента')
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)
    
    @allure.step('Ожидать загрузки страницы')
    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )