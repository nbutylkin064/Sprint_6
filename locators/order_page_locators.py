from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первая страница заказа
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//li[1]")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Вторая страница заказа
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    
    # Локаторы для срока аренды - все возможные варианты
    RENTAL_PERIOD_CONTAINER = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_PERIOD_PLACEHOLDER = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_ARROW = (By.CLASS_NAME, "Dropdown-arrow")
    RENTAL_PERIOD_MENU = (By.CLASS_NAME, "Dropdown-menu")
    RENTAL_PERIOD_OPTIONS = (By.XPATH, "//div[@class='Dropdown-option']")
    
    # Альтернативные локаторы для опций
    RENTAL_OPTION_1 = (By.XPATH, "//div[text()='сутки']")
    RENTAL_OPTION_2 = (By.XPATH, "//div[text()='двое суток']")
    RENTAL_OPTION_3 = (By.XPATH, "//div[text()='трое суток']")
    RENTAL_OPTION_4 = (By.XPATH, "//div[text()='четверо суток']")
    RENTAL_OPTION_5 = (By.XPATH, "//div[text()='пятеро суток']")
    RENTAL_OPTION_6 = (By.XPATH, "//div[text()='шестеро суток']")
    RENTAL_OPTION_7 = (By.XPATH, "//div[text()='семеро суток']")
    
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    
    # Подтверждение заказа
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    
    # Заголовок второй страницы
    RENT_HEADER = (By.XPATH, "//div[contains(@class, 'Order_Header') and text()='Про аренду']")