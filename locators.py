from selenium.webdriver.common.by import By

class TestLocators:
    #==================== Кнопки
    # "Вход и регистрация"
    LOGIN_BUTTON= (By.XPATH, '//button[contains(text(), "Вход и регистрация")]')
    # "Нет аккаунта"
    NO_ACCOUNT_BUTTON = (By.XPATH,'//button[contains(text(),"Нет аккаунта")]')
    #Создать аккаунт
    CREATE_ACCOUNT_BUTTON = (By.XPATH,'//button[contains(text(), "Создать аккаунт")]')
    # "Разместить объявления"
    PLACE_ADVERTISEMENT_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    # Войти
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    # Аватар
    AVATAR_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
    # Выйти
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    # Опубликовать
    PUBLISH_BUTTON= (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    #===================== Поля регистрации
    # поле email
    EMAIL_INPUT= (By.NAME, "email")
    # поле пароля
    PASSWORD_INPUT= (By.NAME, "password")
    # поле повторить пароль
    SUBMIT_PSW_INPUT= (By.NAME, "submitPassword")
    # поле User
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    #===================== Красная полоса на полях
    EMAIL_RED_FIELD = (By.XPATH,
        "//input[@name='email']/parent::div[contains(@class, 'input_inputError__fLUP9')]")
    PASSWORD_RED_FIELD = (By.XPATH,
        "//input[@name='password']/parent::div[contains(@class, 'input_inputError__fLUP9')]")
    SUBMIT_RED_FIELD = (By.XPATH,
        "//input[contains(@name, 'submitPassword')]/parent::div[contains(@class, 'input_inputError__fLUP9')]")
    EMAIL_ERROR = (By.CSS_SELECTOR, ".input_span__yWPqB")
    #================= Окно ввода объявления
    # окно объявления
    WINDOW_ADVERTISEMENT = (By.CSS_SELECTOR, ".homePage_modal__zSdUB")
    # надпись сверху охна
    WINDOW_TITLE = (By.CSS_SELECTOR, ".homePage_modal__zSdUB h1.h1")
    #Название объявления
    ADV_NAME = (By.NAME, "name")
    #Описание объявления
    ADV_DESCRIPTION = (By.NAME, "description")
    #Стоимость
    ADV_PRICE = (By.NAME, "price")
    #Категория
    ADV_CATEGORY_INPUT = (By.XPATH, "//input[@name='category' and @readonly]")
    ADV_CATEGORY_SELECT =(By.XPATH, "//*[contains(text(), 'Авто')]")
    ADV_CITY = (By.XPATH, "//input[@name='city']")
    ADV_CITY_SELECT = (By.XPATH, "//*[contains(text(), 'Москва')]")




