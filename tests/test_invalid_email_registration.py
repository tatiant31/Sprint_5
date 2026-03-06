from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from data import INVALID_USER
from locators import TestLocators

class TestInvalidEmailRegistration:
    def test_invalid_email_registration(self, driver):
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
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(INVALID_USER.email)
        # нажать кнопку «Создать аккаунт».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (TestLocators.CREATE_ACCOUNT_BUTTON)).click()
        # Ждем появление ошибки
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, ".input_inputError__fLUP9")))
        # проверка красной подсветки для поля Email
        email_field = driver.find_element(*TestLocators.EMAIL_RED_FIELD)
        assert "input_inputError__fLUP9" in email_field.get_attribute("class")
        print(" ✓ Email поле подсвечен красным")
        # проверка Ошибка под полем "Email"
        error_message = driver.find_element(*TestLocators.EMAIL_ERROR)
        assert error_message.text == "Ошибка"
        print("✓ Сообщение 'Ошибка' отображается")
        # проверка красной подсветки для поля "Пароль"
        password_field = driver.find_element(*TestLocators.PASSWORD_RED_FIELD)
        assert "input_inputError__fLUP9" in password_field.get_attribute("class")
        print("✓ Пароль контейнер подсвечен красным")
        # проверка красной подсветки для поля "Повторите Пароль"
        submit_password_field = driver.find_element(*TestLocators.SUBMIT_RED_FIELD)
        assert "input_inputError__fLUP9" in submit_password_field.get_attribute("class")
        print("✓ Повтор пароля контейнер подсвечен красным")



