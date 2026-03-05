from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import data
from tests.locators import AuthorisationLocators

class TestUserRegistration:

    def test_registration(self, driver, data_for_registration):
        driver.get(data.URL)
        # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.LOGIN_BUTTON)).click()
        # ожидать загрузку страницы и нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.NO_ACCOUNT_BUTTON)).click()
        # Заполнить все поля формы регистрации
        # Заполнить поле email
        driver.find_element(*AuthorisationLocators.EMAIL_INPUT).send_keys(data_for_registration['email'])
        # Заполнить пароль
        driver.find_element(*AuthorisationLocators.PASSWORD_INPUT).send_keys(data_for_registration['password'])
        # Заполнить повторный пароль
        driver.find_element(*AuthorisationLocators.SUBMIT_PSW_INPUT).send_keys(data_for_registration['password'])
        # нажать кнопку «Создать аккаунт».
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.CREATE_ACCOUNT_BUTTON)).click()
        print(f"Регистрация с email: {data_for_registration['email']}, password: {data_for_registration['password']}")
        #Проверить: произошёл переход на главную страницу, в правом верхнем углу
        # около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        # Проверить Кнопка «Разместить объявление» присутствует
        place_ad_btn = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (AuthorisationLocators.PLACE_ADVERTISEMENT_BUTTON))
        assert place_ad_btn.is_displayed(), "Кнопка 'Разместить объявление' не отображается"

        # Проверить кнопку аватара (circleSmall) - она есть на главной странице
        avatar_button = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (AuthorisationLocators.AVATAR_BUTTON))
        assert avatar_button.is_displayed(), "Кнопка аватара (circleSmall) не отображается"

        # Проверить в правом верхнем углу отображается аватар и имя "User"
        user_name_element = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located
            (AuthorisationLocators.USER_NAME))
        assert user_name_element.text.strip() == "User.", f"Ожидалось 'User.', получено: '{user_name_element.text}'"
        print("Пользователь авторизован: Аватар + User. + кнопка Разместить объявление")
        print(f"Текущий URL: {driver.current_url}")
        print(f"Успешная регистрация: {data_for_registration['email']}")
