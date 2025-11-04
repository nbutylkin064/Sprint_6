from selenium.webdriver.common.by import By


class MainPageLocators:
    # Главная страница
    MAIN_HEADER = (By.XPATH, "//div[contains(@class, 'Home_Header')]")
    
    # Вопросы о важном
    FAQ_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")
    FAQ_QUESTIONS = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"), 
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7")
    }
    FAQ_ANSWERS = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7")
    }
    
    # Кнопки заказа
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
    ORDER_BUTTON_MAIN = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    
    # Логотипы
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    