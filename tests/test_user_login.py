from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests import data
from tests.locators import AuthorisationLocators

class TestUserLogin:
    def test_user_login(self, driver):
        driver.get(data.URL)
        # Ожидать загрузку страницы и нажать кнопку «Вход и регистрация».
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable
            (AuthorisationLocators.LOGIN_BUTTON)).click()
        # Заполняем email
        driver.find_element(*AuthorisationLocators.EMAIL_INPUT).send_keys(data.user_email)
        # Заполнить пароль
        driver.find_element(*AuthorisationLocators.PASSWORD_INPUT).send_keys(data.user_password)
        # Нажать кнопку Войти
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(AuthorisationLocators.ENTER_BUTTON)).click()
        #Проверить: произошёл переход на главную страницу, в правом верхнем углу
        #около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
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
            expected_conditions.presence_of_element_located(
                AuthorisationLocators.USER_NAME))
        assert user_name_element.text.strip() == "User.", f"Ожидалось 'User.', получено: '{user_name_element.text}'"
        print("Пользователь авторизован: Аватар + User. + кнопка Разместить объявление")
        print(f"Текущий URL: {driver.current_url}")

