from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import data
from data import *

fake = Faker('en_US')
# генерация email и пароля
def data_for_registration() -> RegData:
    #Возвращает объект RegData с фейковыми данными
    return RegData(
        email=fake.email(),
        password=fake.password(length=12)
    )

# Регистрация нового пользователя
def register_new_user(driver):
    driver.get(data.URL)
    # cгенерировали email и password
    user = data_for_registration()
    # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable
        (TestLocators.LOGIN_BUTTON)).click()
    # ожидать загрузку страницы и нажать кнопку «Нет аккаунта».
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable
        (TestLocators.NO_ACCOUNT_BUTTON)).click()
    # Заполнить все поля формы регистрации
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(user.email)
    # Заполнить пароль
    driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(user.password)
    # Заполнить повторный пароль
    driver.find_element(*TestLocators.SUBMIT_PSW_INPUT).send_keys(user.password)
    # нажать кнопку «Создать аккаунт».
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable
        (TestLocators.CREATE_ACCOUNT_BUTTON)).click()

# ввод зарегистрированного пользователя
def login_user(driver):
    driver.get(data.URL)
    # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable
        (TestLocators.LOGIN_BUTTON)).click()
    # Заполняем email
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(TestUsers.VALID_USER.email)
    # Заполнить пароль
    driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(TestUsers.VALID_USER.password)
    # Нажать кнопку Войти
    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable(TestLocators.ENTER_BUTTON)).click()

# выйти из профайла
def login_and_logout(driver):
   login_user(driver)
   #Нажать кнопку Выйти
   WebDriverWait(driver, 5).until(
       expected_conditions.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click()


# ввод существующего  email
def register_existing_user(driver):
    driver.get(data.URL)
    # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable
        (TestLocators.LOGIN_BUTTON)).click()
    # ожидать загрузку страницы и нажать кнопку «Нет аккаунта».
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable
        (TestLocators.NO_ACCOUNT_BUTTON)).click()
    # Заполнить все поля формы регистрации
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(TestUsers.VALID_USER.email)
    driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(TestUsers.VALID_USER.password)
    driver.find_element(*TestLocators.SUBMIT_PSW_INPUT).send_keys(TestUsers.VALID_USER.password)
    # нажать кнопку «Создать аккаунт».
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable
        (TestLocators.CREATE_ACCOUNT_BUTTON)).click()

# ввод невалидного email
def invalid_email_registration(driver):
    driver.get(data.URL)
    # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable
        (TestLocators.LOGIN_BUTTON)).click()
    # ожидать загрузку страницы и нажать кнопку «Нет аккаунта».
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable
        (TestLocators.NO_ACCOUNT_BUTTON)).click()
    # Заполнить поле Email формы регистрации
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(TestUsers.INVALID_USER.email)
    # нажать кнопку «Создать аккаунт».
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable
        (TestLocators.CREATE_ACCOUNT_BUTTON)).click()

