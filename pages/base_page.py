import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Найти элементы')
    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Кликнуть на элемент')
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Кликнуть на элемент через JavaScript')
    def click_via_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Кликнуть на элемент через ActionChains')
    def click_via_action_chains(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()

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

    @allure.step('Проверить, что элемент видим')
    def is_element_visible(self, locator):
        try:
            return EC.visibility_of_element_located(locator)(self.driver)
        except:
            return False

    @allure.step('Ожидать появления элемента')
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидать кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Ожидать исчезновения элемента')
    def wait_for_element_to_disappear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Ожидать загрузки страницы')
    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )